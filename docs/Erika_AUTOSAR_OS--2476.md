# Erika AUTOSAR OS

<a id="Multicore_Autosar_OS_Support"></a>

## Multicore Autosar OS Support

ERIKA support multicore environments a way before than the first Autosar Multicore OS Release. So it happened that the historical [ERIKA multicore support](ERIKA_multicore_support--2066.md "ERIKA multicore support") addresses some of the same requiremets of AUTOSAR Multicore OS with a completely different policy.

In detail all the primitives calls on other core, with traditional implementation, called **Remote Notifications** or **RN**, are done **asynchronously** with a fire and forget policy. This approach reduce latency to minimun, but, on the other hand, don't give the opportunity to check for errors in the call site.

Autosar, that take into account a way more code consistency and reliability than efficiency, requires that all the primitives calls on others cores are **synchronous** giving the opportunity to caller code to correctly handle errors.

To implements Autosar OS requirements a completly new multicore dispatcher have been implemented. This have been called
**ERIKA Autosar RPC** (Remote Procedure Call).

<a id="Difference_between_the_traditional_RN_implementation_and_the_new_RPC_implementation"></a>

### Difference between the traditional RN implementation and the new RPC implementation

The **RN** implementation is the original implementation done in 2002 of the MSRP protocol proposed in the paper

```
  Minimizing memory utilization of real-time task sets in single and multi-processor systems-on-a-chip
  P Gai, G Lipari, M Di Natale
  Real-Time Systems Symposium, 2001.(RTSS 2001). Proceedings. 22nd IEEE, 73-83
```

which included the following features:

- ASYNCHRONOUS remote activation of tasks. Activations are queued for later processing. Spin lock time is minimized. Local primitives returns E\_OK despite the result of the remote activation (errors must be caught using ErrorHook!)
- Queuing spin lock implemented using the algorithm presented in

```
 G. Graunke and S. Thakkar, Synchronization algorithms for shared memory multiprocessors. IEEE Computer, 23(6):60-69, June 1990
```

- automatic detection from the OIL file whether resources are global or local. That is, GetResource and ReleaseResource where implementing an additional spin-lock when the resource was global. The idea was that the system allowed migration of tasks from one CPU to another without changing the OS code.

All those points have been partially dropped on some architectures due to some of the requirements of AUTOSAR. In particular, spin-locks have a separate API (so GetResource and ReleaseResource cannot call implicitly a spinlock), and queuing spin-lock is not in the standard and is also quite difficult to implement in an efficient way considering that in some situazion a task can be removed from spinning.

As for the first point, AUTOSAR mandates the fact that priomitives should return the status of the execution of the primitive, ALSO if the execution happens on the remote core. This implies that the remote activations must be SYNCHRONOUS. That is the reason why we created the **RPC** implementation, which has the following features:

- SYNCHRONOUS remote activation of tasks
- Normal (no protocol) spin-locks to comply with AUTOSAR
- no detection of remote resources, which... does not exist in AUTOSAR

Final note on interprocessor interrupt priorities:

- the interprocessor IRQ must be an ISR2
- on RN, the interprocessor IRQ can be the LOWEST priority interrupt, as the requests are queued and since the spin lock time is independent of the priority of the IRQ.
- on RPC, the spin-lock time highly depends on the interprocessor IRQ RESPONSE TIME, which is affected by its priority. Therefore, the interprocessor Interrupt should have a HIGH priority, and this means that mopre and more IRQs must become ISR2 (remember ISR1 must have highet priority than ISR2), making the implementation more and more inefficient.

<a id="How_to_select_the_traditional_RN_implementation_and_the_new_RPC_implementation"></a>

### How to select the traditional RN implementation and the new RPC implementation

Both traditional and the new dispatcher are available for Infineon AURIX and Freescale PowerPC (MPC5777C). You can switch between them in OIL with the REMOTENOTIFICATION oil field.

```
 REMOTENOTIFICATION = USE_RN;
```

Enable traditional **Remote Notification** dispatcher. It's the default value, so you don't need to write this.

```
 REMOTENOTIFICATION = USE_RPC;
```

Enable the new **AUTOSAR Remote Procedure Call** dispatcher.

Currently with the new RPC dispatcher you can execute on remote cores all the following primitives:

- ActivateTask
- ChainTask (Terminate local TASK but can schedule on remote core)
- GetTaskState
- SetEvent
- GetAlarmBase
- GetAlarm
- SetRelAlarm
- SetAbsAlarm
- CancelAlarm
- GetCounterValue
- GetElapsedValue
- ShutdownOS ( with new ShutdownAllCores API )

So in addition to TASK and EVENT primitives, the new muticore dispatcher support Counters and Alarms as required by Autosar specifications. Multicore awareness have been added to ShutdownOS to fulfill multicore AUTOSAR shutdown sequence.

<a id="New_Multicore_API"></a>

### New Multicore API

AUTOSAR expect a master/slaves multicore enviroment that naturally fit AURIX architecture.
New API to start and stops slave cores specified in AUTOSAR v4.0 rev 3.0 have been added:

- **StartCore**: This function starts the core specified by the parameter CoreID. The OUT parameter allows the caller to check whether the operation was successful or not. If a core is started by means of this function **StartOS** shall be called on the core. It is not supported to call this function after **StartOS()**.
- **StartNonAutosarCore**: The function starts the core specified by the parameter CoreID. It **is allowed** to call this function after **StartOS()**. The OUT parameter allows the caller to check whether the operation was successful or not. It is **not allowed to call StartOS** on cores activated by **StartNonAutosarCore**.
- **GetNumberOfActivatedCores**: returns the number of cores activated by the StartCore function. This function might be a macro
- **GetCoreID**: The function returns a unique core identifier.
- **ShutdownAllCores** : After this service the OS on all AUTOSAR cores is shut down. Allowed at TASK level and ISR level and also internally by the OS. The function will never return. The function will force other cores into a shutdown.

<a id="New_Spinlocks_API"></a>

### New Spinlocks API

Support for AUTOSAR Spinlock API have been added. OIL implementation have been extended to support Spinlocks configuration.

There's two spinlocks behaviour modes: **SINGLE** and **ORDERED**. If **SINGLE** mode is configured a core get an error if, holding a spinlock, try to get access to another one. If **ORDERED** mode is configurated the core get this error only if it try to get spinlocks out of the order (see AUTOSAR documentation paragraph 7.9.29 The spinlock mechanism).

To configure spinlocks in **SINGLE** mode, just don't provide any order:

```
 SPINLOCK spinlock_1 {  };
 SPINLOCK spinlock_2 {  };
 SPINLOCK spinlock_3 {  };
```

To configure spinlocks in **ORDERED** mode provide a **complete ordering**:

```
 SPINLOCK spinlock_1 { NEXT_SPINLOCK=spinlock_2; };
 SPINLOCK spinlock_2 { NEXT_SPINLOCK=spinlock_3; };
 SPINLOCK spinlock_3 {  };
```

Provided AUTOSAR API to interact with Spinlocks are:

- **GetSpinlock** : Tries to occupy a spin-lock variable. If the function returns, either the lock is successfully taken or an error has occurred. The spinlock mechanism is an active polling mechanism. The function does not cause a de-scheduling.
- **ReleaseSpinlock**: Releases a spinlock variable that was occupied before. Before terminating a TASK all spinlock variables that have been occupied with GetSpinlock() shall be released. Before calling WaitEVENT all Spinlocks shall be released.
- **TryToGetSpinlock**: Has the same functionality as GetSpinlock with the difference that if the spinlock is already occupied by a TASK on a different core the function sets the OUT parameter to TRYTOGETSPINLOCK\_NOSUCCESS and returns with E\_OK.

Two spinlocks implementation are provided. The **trivial** one that does not guarentee upper bond wait, but that can implement the try-to-get behaviour. And the **queued** one that prevent from starvation queuing requests, but cannot implement try-to-get behaviour (TryToGetSpinlock API is mapped into GetSpinlock).

To enable **queued spinlocks** just add to the OIL:

```
 SPINLOCKS = QUEUED;
```

IMPORTANT: QUEUED spinlocks are not available for Erika on PowerPC.

<a id="Autosar_Schedule_Tables"></a>

## Autosar Schedule Tables

Autosar Specification add to OSEK Alarms, another activities schedulator called Schedule Tables.
It is possible to implement a statically defined activities schedulator, that activate TASKs and set EVENTs, using an
OSEK counter and a series of auto started alarms. In the simple case, this can be achieved by specifying that the alarms are not modified once started. Run-time modifications can only be made if relative synchronization between alarms can be
guaranteed.This typically means modifying the alarms while associated counter tick interrupts are disabled.
Schedule Tables address the synchronization issue by providing an encapsulation of a statically defined set of expiry points. Each expiry point defines:

- One or more actions that must occur when it is processed where an action is the activation of a task or the setting of an event.
- An offset in ticks from the start of the schedule table.

Each schedule table has a duration in ticks. The duration is measured from zero and
defines the modulus of the schedule table.

At runtime, the Operating System module will iterate over the schedule table, processing each expiry point in turn. The iteration is driven by an OSEK counter. It therefore follows that the properties of the counter have an impact on what is possible to configure on the schedule table.

<a id="Schedule_Table_APIs"></a>

### Schedule Table APIs

All the Schedule Table API not related to the schedule table syncronization are implemented (see [Schedule Table Synchronization](Erika_AUTOSAR_OS--2476.md#Schedule_Table_Synchronization "Erika AUTOSAR OS")).

- **StartScheduleTableRel( ScheduleTableType ScheduleTableID, TickType Offset )**: This service starts the processing of a schedule table at "Offset" relative to the "Now" value on the underlying counter.

- **StartScheduleTableAbs( ScheduleTableType ScheduleTableID, TickType Start )**: This service starts the processing of a schedule table at an absolute value "Start" on the underlying counter.

- **StopScheduleTable( ScheduleTableType ScheduleTableID )**: This service cancels the processing of a schedule table immediately at any point while the schedule table is running.

- **GetScheduleTableStatus( ScheduleTableType ScheduleTableID, ScheduleTableStatusRefType ScheduleStatus )**: This service queries the state of a schedule table (also with respect to synchronization).

- **NextScheduleTable(ScheduleTableType ScheduleTableID\_From, ScheduleTableType ScheduleTableID\_To)**: This service switches the processing from one schedule table to another schedule table.

**N.B.** The best place to start to understand how schedule tables API works is:
*tricore/infineon\_TriBoard-TC2X5\_V2.0/Schedule Tables/Schedule Table example*

<a id="Schedule_Table_OIL_Configuration"></a>

### Schedule Table OIL Configuration

This is an OIL example to how configure a Schedule Table with OIL

```
 SCHEDULETABLE SchedTab1 {
   COUNTER = system_timer;
   DURATION = 400;
   REPEATING = FALSE;
   AUTOSTART = TRUE {
     TYPE = ABSOLUTE;
     START_VALUE = 0;
   };
   EXPIRE_POINT = ACTION {
     EXPIRE_VALUE = 100;
     ACTION = ACTIVATETASK { TASK = Task2; };
     ACTION = SETEVENT { TASK = Task1; EVENT = ButtonEvent; };
     SYNC_ADJUSTMENT = FALSE;
   };
   EXPIRE_POINT = ACTION {
     EXPIRE_VALUE = 300;
     ACTION = SETEVENT { TASK = Task1; EVENT = TimerEvent; };
     SYNC_ADJUSTMENT = FALSE;
   };
   LOCAL_TO_GLOBAL_TIME_SYNCHRONIZATION = FALSE;
 };
```

Following the SCHEDULETABLE field explaination

- **COUNTER**: The Schedule Table **driving counter**
- **DURATION**: The Schedule Table duration (in counter ticks), MUST be greater or equal to the last EXPIRE\_POINT.EXPIRE\_VALUE
- **REPEATING**: Flag if the Schedule Table is one shot or have to be restarted when it terminated (after DURATION ticks).
- **AUTOSTART**: Flag if the Schedule Table have to be started automatically during *StartOs*, in which way **TYPE**: (ABSOLUTE, RELATIVE) and with wich Start Value of the counter (or Offset if the TYPE is RELATIVE). In ERIKA where, all the counters are software the two autostartig type generate the same result.
- **EXPIRE\_POINT**: **List of EXPIRY\_POINT** that represent the Schedule Table, any of which is composed by an **EXPIRE\_VALUE** in ticks (when the expiry points happens) a **list of ACTIONS** (*equals to ALARMs Actions*) and by a flag that enable synchronization not yet supported (SYNC\_ADJUSTMENT. Only FALSE value is supported, that is the default so the field can be omitted).

**LOCAL\_TO\_GLOBAL\_TIME\_SYNCHRONIZATION**: Flag that enable External Syncronization, not supported yet. (Only FALSE value is supported, that is the default so the field can be omitted).

**N.B.** The best place to start to understand how schedule tables OIL configuration works is:
*tricore/infineon\_TriBoard-TC2X5\_V2.0/Schedule Tables/Schedule Table example*

<a id="Schedule_Table_Synchronization"></a>

### Schedule Table Synchronization

The absolute time at which the Initial Expiry Point on a schedule table is processed is under user control. However, if the schedule table repeats then it is not guaranteed that the absolute count value at which the initial expiry point was first processed is the same count value at which it is subsequently processed. This is because the duration of the schedule table need not be equal to the counter modulus.
In many cases it may be important that schedule table expiry points are processed at specific absolute values of the underlying counter. This is called synchronization. Typical use-cases include:

- Synchronization of expiry points to degrees of angular rotation for motor management
- Synchronizing the computation to a global (network) time base.

Note that in AUTOSAR, the Operating System does not provide a global (network) time source because

- 1. A global time may not be needed in many cases
- 2. Other AUTOSAR modules, most notably FlexRay, provide this independently to the Operating System
- 3. If the Operating System is required to synchronize to multiple global (network) time sources (for example when building a gateway between two time-triggered networks) the Operating System cannot be the source of a unique global time. AUTOSAR OS provides support for synchronization in two ways:

- 1. Implicit Synchronization – The counter driving the schedule table is the counter with which synchronization is required. This is typically how synchronization with time-triggered networking technologies (e.g. FlexRay, TTP) is achieved – the underlying hardware manages network time synchronization and simply presents time as an output/compare timer interface to the Operating System.
- 2. Explicit Synchronization – The schedule table is driven by an Operating System counter which is not the counter with which synchronization is required. The Operating System provides additional functionality to keep schedule table processing driven by the Operating System counter synchronized with the synchronization counter. This is typically how synchronization with periodically broadcast global times works.

**N.B.** Explicity synchronization is not fully supported yet. (**SyncScheduleTable** have been implemented but not yet tested. **StartScheduleTableSynchron** and **SetScheduleTableAsync** are not implemented at all).

<a id="Autosar_OSApplication_and_Protection_Support"></a>

## Autosar OSApplication and Protection Support

AUTOSAR specifications introduce OS-Applications as entities containers (TASKs, ISR2s, COUNTERs, ALARMS, Schedule Tables), that could resemble to processes (without memory virtualization).

The Operating System module is responsible for scheduling the available processing resource between the OS-Applications that share the processor. If OS-Application(s) are used, all TASKs, ISRs, COUNTERs, ALARMs and Schedule tables must belong to an OS-Application. All objects which belong to the same OS-Application have access to each other. The right to access objects from other OS-Applications may be granted during configuration. An event is accessible if the TASK for which the EVENT can be set is accessible. Access means that these Operating System objects are allowed as parameters to API services.

The above are the foundamentals of  [Service Protection](Erika_AUTOSAR_OS--2476.md#Service_Protection "Erika AUTOSAR OS").

There are two classes of OS-Application:

- 1 **Trusted OS-Applications**: Are allowed to run with monitoring or protection features disabled at runtime. They may have unrestricted access to memory, the Operating System module’s API, and NEED NOT have their timing behaviour enforced at runtime. They are allowed to run in privileged mode when supported by the processor.

- 2 **Non-Trusted OS-Applications**: Are not allowed to run with monitoring or protection features disabled at runtime. They have restricted access to memory, restricted access to the Operating System module’s API and have their timing behaviour enforced at runtime. They are not allowed to run in privileged mode when supported by the processor.

Operating System module itself is a TRUSTED OS-Application.

The running OS-Application is defined as the OS-Application to which the currently running Task or ISR belongs. In case of a hook routine the Task or ISR which caused the call of the hook routine defines the running OS-Application.

There are services offered by the AUTOSAR OS which give the caller information about the access rights and the membership of objects and memory variables. These services are intended to be used in case of an inter-OS-Application call for checking access rights and arguments.

OS-Applications have a state which defines the scope of accessability of its Operating System objects from other OS-Applications. Each OS-Application is always in one of the following states:

- **Active and accessible** (APPLICATION\_ACCESSIBLE): Operating System objects may be accessed from other OS-Applications. This is the default state at startup.
- **Currently in restart phase** (APPLICATION\_RESTART): Operating System objects can not be accessed from other OS-Applications. State is valid until the OSApplication calls AllowAccess().
- **Terminated and not accessible** (APPLICATION\_TERMINATED): Operating System objects can not be accessed from other OS-Applications. State will not change.

Protection is only possible for Operating System managed objects. This means that:

- It is not possible to provide protection during runtime of Category 1 ISRs, because the operating system is not aware of any Category 1 ISRs being invoked. Therefore, if any protection is required, Category 1 ISRs have to be avoided. If Category 1 interrupts AND OS-Applications are used together then all Category 1 ISR must belong to a trusted OS-Application.
- It is not possible to provide protection between functions called from the body of the same Task/Category 2 ISR.

Autosar specify four protection features:

- **Service Protection**: Protect the Object Access (TASK, ALARMs, Schedule Table, Resources) between OS-Application, if the permission is not explicitly granted.
- **Memory Protection**: Protect **Global Data** and **Stacks** of an OS-Application from possible corruption by Non-Trusted OS-Application.
- **Stack Monitoring**: On processors that do not provide any memory protection hardware it may still be necessary to provide a “best effort with available resources” scheme for detectable classes of memory faults. Stack monitoring will identify where a task or ISR has exceeded a specified stack usage at context switch time.
- **Timing Protection**: A timing fault in a real-time system occurs when a task or interrupt misses its deadline at runtime. Autosar OS supply a mechanism based on budget that let the software understand which TASK or ISR2 is causing a deadline missing

<a id="OS-Application_API_.26_OIL_Configuration"></a>

### OS-Application API & OIL Configuration

The OS-Applications life-cycle is controlled by two APIs **TerminateApplication** and **AllowAccess**. TerminateApplication **stops** OS-Applications' **active and ready** instances of **TASKs and ISR2s** and won't schedule them more as long as the application is possibly restarted, plus make all the its objects inaccessible, this means, for example, that won't be possible to read a counter or set an alarm of the given OS-Application.

This is useful to stop a faulty portion of the firmware (this usually can happens automatically when ProtectionHook is configured) or to change the configuration of the application it self in case of, for example, power saving mode.

When **TerminateApplication** is called with **RESTART** as restart option just one istance of a pre-configured terminated OS-Application's TASK is activated and schedulated. This and only this TASK can put OS-Application's data in a consitent configuration and then call **AllowAccess** API to actually Restart the OS-Application.

Following the list of the API that directly interact with OS-Application.

- **TerminateApplication**( ApplicationType Application, RestartType RestartOption ): Restart OS-Application "Application", if RestartOption is equal to RESTART, or completly terminate it, if RestartOption is equal to NO\_RESTART. Restart an OS-Application is a termination with the automatic schedulation of OIL APPLICATION.RESTARTTASK that can reset OS-Application to a consistent status and call AllowAccess to actually restart the application. So only OS-Application that have OIL APPLICATION.RESTARTTASK field configurated can be effectively restarted.
- **AllowAccess**( void ): Can be called only by an OS-Application Restarting TASK and only when the OS-Application is effectively restarting, to reset OS-Application status to accessibile.

The **OIL configuartion container**:

**N.B.** Remember that if OS-Application are used EVERY SINGLE OBJECT have to belong to an OS-Application, but RESOURCEs, EVENTs and those that impicitly belong to OS, like SYSTEM\_TIMER COUNTER.

```
 APPLICATION App1 {
   TRUSTED = FALSE;
   TASK    = App1Task1;
   TASK    = App1Task2;
   TASK    = App1Task3;
   COUNTER = App1Counter1;
   COUNTER = App1Counter2;
   ALARM   = App1Alarm1;
   ALARM   = App1Alarm2;
   SCHEDULETABLE = App1ScheduleTable;
   SCHEDULETABLE = App1ScheduleTable;
   //MEMORY_SIZE = 0x1000;
   SHARED_STACK_SIZE = 256;
   IRQ_STACK_SIZE = 256;
   RESTARTTASK = App1Task3;
 };
```

- **TRUSTED**: Flag if the OS-Application is Trusted or not. BE AWARE TO REDUCE TO MINIMUM THE USE OF TRUSTED OS-APPLICATIONS, BECAUSE THEY BYPASS MEMORY PROTECTION (if enabled).
- **TASK**: **List** of all the TASKs that belong to the OS-Application.
- **COUNTER**: **List** of all the COUNTERs that belong to the OS-Application.
- **ALARM**: **List** of all the COUNTERs that belong to the OS-Application.
- **SCHEDULETABLE**: **List** of all the SCHEDULETABLEs that belong to the OS-Application.
- **MEMORY\_SIZE**: This Parameter is an ERIKA's extension to AUTOSAR. When this parameter is set enable an ASSERTION test in ELF linkin tha assure that the RAM used by the application (DATA + STACKs) is less or equal of MEMORY\_SIZE.
- **SHARED\_STACK\_SIZE**: Stack's size for all the OS-Application's TASKs configured to share the stack (Container TASK field STACK = SHARED).
- **IRQ\_STACK\_SIZE**: Stack's size for all the OS-Application's ISR2s.

<a id="Service_Protection"></a>

### Service Protection

As OS-Applications can interact with the Operating System module through services, it is essential that the service calls will not corrupt the Operating System module itself. **Service Protection guards against such corruption at runtime**.

There are a number of cases to consider with **Service Protection:**

**An OS-Application makes an API call**

- **(1) with an invalid handle or out of range value.**
- **(2) in the wrong context, e.g. calling ActivateTask() in the StartupHook().**
- **(3) or fails to make an API call that results in the OSEK OS being left in an undefined state, e.g. it terminates without a ReleaseResource() call**
- **(4) that impacts on the behaviour of every other OS-Application in the system, e.g. ShutdownOS()**
- **(5) to manipulate Operating System objects that belong to another OS-Application (to which it does not have the necessary permissions), e.g. an OS-Application tries to execute ActivateTask() on a task it does not own.**

The OSEK OS already provides some service protection through the status codes returned from service calls and this will provide the basis for service protection. This means that service protection will only apply for the extended status of OSEK OS.
However, OSEK OS does not cover all the cases outlined above.

The **Service Protection** sit on top of OS-Application configuration. So Service Protection **CANNOT BE ENABLED WITHOUT PROVIDING A FULL OS-Applications CONFIGUARTION**

To enable Service Protection the following OIL field can be specified:

```
 SERVICE_PROTECTION = TRUE;
```

With this flag enabled and without accessing rules specified, TASK and ISR2 can access only the objects that belong to its own OS-Application.

If accessing rules for OBJECTS are explicitly provided (see below) the Service Protection OIL flag is optional.

**N.B.: Enabling Service protection (explicitly, with OIL SERVICE\_PROTECTION flag, or implicitly, providing Objects accessing rules) with OSEK STATUS configured as standard (STATUS=STANDARD) is considered an incongruent configuration according AUTOSAR specification and should be avoided (RT-Druid will complain with a warning).**

To explicitly provide access privileges to objects to other OS-Application, accessing fields have to be added to specified objects:

```
 TASK Task1 {
   ....
   ACCESSING_APPLICATION = App2;
 };
 
 COUNTER Counter2 {
   ...
   ACCESSING_APPLICATION = App1;
   ACCESSING_APPLICATION = App3;
 };
 
 ALARM Alarm2 {
   COUNTER = Counter2;
   ...
   ACCESSING_APPLICATION = App1;
   ACCESSING_APPLICATION = App3;
   ACCESSING_APPLICATION = App4;
 };
 
 SCHEDULETABLE ScheduleTable2 {
   COUNTER = CounterSlave2;
   ... 
   ACCESSING_APPLICATION = App1;
   ACCESSING_APPLICATION = App4;
 };
```

<a id="Memory_Protection"></a>

### Memory Protection

Memory protection will only be possible on processors that provide hardware support for memory protection.
AUTOSAR memory protection scheme is based on the (data, code and stack) sections of the executable program. ERIKA's implementation take AUTOSAR requirements in the following way:

- **Stack:** To keep context change still efficient and let the ERIKA's Stack sharing optimizzation still usable. All the stack space is accessible by all the OS-Application's TASK and ISR2 (In particualr ISR2s supports only stack sharing policy, so it's not possible specify a private stack for a ISR2).
- **Data:** There is no TASK's or ISR2's private global data space, only OS-Application's globa ldata space is implemented.
- **Code:** All the code is Shared. Data protection protect from data structures corruption.

The **Memory Protection** sit on top of OS-Application configuration. So Memory Protection **CANNOT BE ENABLED WITHOUT PROVIDING A FULL OS-Applications CONFIGURATION**

To enable Memory Protectionion the following OIL field can be specified:

```
 MEMORY_PROTECTION = TRUE;
```

**TASKs and and ISR2s of a NON-TRUSTED OS-Application can only access global data that belong to OS-Application global data space.**

To locate a variable in the right section, MemMap.h header file feature should be used.

<a id="MemMap.h_header_file_Rationale_and_Use"></a>

#### MemMap.h header file Rationale and Use

**MemMap.h** file is the standar AUTOSAR tool to be used to handle the problem to locate data e code of an application in a compiler agnostic way. ERIKA's build chain, Starting from OIL OS-Application's configuration, will generate a **MemMap.h** that contains.

For each OS-Application are reserved three sections:

- **ee\_${APP\_NAME}\_bss**: To locate OS-Application's uninitialized variables.
- **ee\_${APP\_NAME}\_data**: To locate OS-Application's initialized variables.
- **ee\_${APP\_NAME}\_text**: To locate OS-Application's code (it is a predisposition to Code protection, not effectively used yet).

With parameter substitution of ${APP\_NAME} with the real OIL OSAPPLICATION Field Name.

The sum of **ee\_${APP\_NAME}\_bss** and **ee\_${APP\_NAME}\_data** section will compose the **OS-Application private data space**.

To add some variables or code to a OS-Application you have to use the following *commands* Macro defined right before
the MemMap inclusion:

- **APP\_${APP\_NAME}\_START\_SEC\_VAR\_NOINIT/APP\_${APP\_NAME}\_STOP\_SEC\_VAR\_NOINIT**
- **APP\_${APP\_NAME}\_START\_SEC\_DATA/APP\_${APP\_NAME}\_STOP\_SEC\_DATA**
- **APP\_${APP\_NAME}\_START\_SEC\_CODE/APP\_${APP\_NAME}\_STOP\_SEC\_CODE**

As the following example:

```
 #define APP_App1_START_SEC_VAR_NOINIT
 #include "MemMap.h"
 
 EE_UREG app1_noinit1;
 EE_UREG app1_noinit2;
 
 #define APP_App1_STOP_SEC_VAR_NOINIT
 #include "MemMap.h"
```

```
 #define APP_App1_START_SEC_VAR_DATA
 #include "MemMap.h"
 
 EE_UREG app1_data1 = 1U;
 EE_UREG app1_data2 = 2U;
 
 #define APP_App1_STOP_SEC_VAR_DATA
 #include "MemMap.h"
```

For Communication between OS-Application AUTOSAR introduce **IOC** (Inter OS-Applications Communication) **Mechanism**. An experimental support of **IOC** is provided by ERIKA, but RT-Druid cannot yet configure it, and since the IOC configuration is hard to be done correctly by hand, some special sections are providded that are accessible by ALL OS-Application by default. (It's suggested to reduce at the minimun the data shared between OS-Applications, to not frustrate Memory Protection). These sections are usable with the following MemMap.h *commands* Macros:

- **API\_START\_SEC\_VAR\_NOINIT/API\_STOP\_SEC\_VAR\_NOINIT**
- **API\_START\_SEC\_DATA/API\_STOP\_SEC\_DATA**

<a id="TRSUTED_OS-Application_.26_Trusted_Services_.28TRUSTED_FUNCTION.29"></a>

#### TRSUTED OS-Application & Trusted Services (TRUSTED\_FUNCTION)

An OS-Appilcation, to bypass it's own bounduaries in a "controlled" way, can invoke a Trusted Function provided by (another) trusted OS-Application. That can require a switch from non-privileged to privileged mode. This is typically achieved by these operations:

- (1) Each trusted OS-Application may export services which are callable from other OS-Applications.
- (2) During configuration these trusted services must be configured to be called from a non-trusted OS-Application.
- (3) The call from the non-trusted OS-Application to the trusted service is using a mechanism (e.g. trap/software interrupt) provided by the Operating System. The service is passed as an identifier that is used to determine, in the trusted environment, if the service can be called.
- (4) The Operating System offers services to check if a memory region is write/read/execute accessible from an OS-Application. It also returns information if the memory region is part of the stack space.

This is an example of TRUSTED function interface and OIL Configuration.

**N.B.** If a **"Service Interface"** will be provided (a **Service Interface** is a function that wrap the ERIKA's **CallTrustedFunction** OS API call), as AUTOSAR coding style dictate; this **must be added to the API code section** with the use of **MemMap.h and the *commands* API\_START\_SEC\_CODE/API\_STOP\_SEC\_CODE**. (The use of the Code API Section it's not optinal because, even though Code protection is not implemented yet, inside the ERIKA's syscall handler, the call site address is checked, against Kernel and API boundaries, before to accept the call).

TRUSTED Service Declaration Header File

```
 #define APP_App2Trusted_START_SEC_CODE
 #include "MemMap.h"
 /* TRUSTED Service */
 StatusType TRUSTED_TrustedService1 (TrustedFunctionIndexType index, TrustedFunctionParameterRefType ref);
 #define  APP_App2Trusted_STOP_SEC_CODE
 #include "MemMap.h"
 
 #define API_START_SEC_CODE
 #include "MemMap.h"
 /* User inteface */
 StatusType CallTrustedService1 ( void );
 #define API_STOP_SEC_CODE
 #include "MemMap.h"
```

TRUSTED Service Definition File

```
 /* User inteface */ 
 StatusType CallTrustedService1 ( void )
 {
   /* User inteface Implementation */
   return CallTrustedFunction(EE_ID_TRUSTED_TrustedService1, NULL);
 }
 
 /* TRUSTED Service Implementation */
 StatusType TRUSTED_TrustedService1 (TrustedFunctionIndexType index,
   TrustedFunctionParameterRefType ref)
 {
   /* TRUSTED Service Implementation */
 }
```

The OIL to configure a TRUSTED services for an Trusted OS-Application

```
 APPLICATION App2Trusted {
   TRUSTED = TRUE { /* <-- OS-Application have to be TRUSTED to have a TRUSTED_FUNCTION */
     TRUSTED_FUNCTION = TRUE {
       NAME = "TrustedService1";
     };
     TRUSTED_FUNCTION = TRUE {
       NAME = "TrustedService2";
     };
     ...
   };
```

<a id="Timing_Protection"></a>

### Timing Protection

A timing fault in a real-time system occurs when a task or interrupt misses its deadline at runtime.
AUTOSAR OS does not offer deadline monitoring for timing protection. Deadline monitoring is insufficient to correctly identify the Task/ISR causing a timing fault in an AUTOSAR system. When a deadline is violated this may be due to a timing fault introduced by an unrelated Task/ISR that interferes/blocks for too long. The fault in this case lies with the unrelated Task/ISR and this will propagate through the system until a Task/ISR misses its deadline. The Task/ISR that misses a deadline is therefore not necessarily the Task/ISR that has failed at runtime, it is simply the earliest point that a timing fault is detected.

AUTOSAR use a budget mechanism to locate the violating entity. The following budgets can be configured:

- **Execution Budget for TASK and ISR2**: This is the ammount of time that a TASK/ISR2 can be executing (RUNNING status for a TASK). **The budget is paused when a TASK/ISR2 is preempted**. The budget is **refilled** when a **TASK/ISR2 terminate** or a **TASK block on a WaitEvent**.
- **Resource Lock Time**: This is the ammount of time that a TASK/ISR2 can lock a specific resource (with the call of **GetResource**). Can be specified for each resource that a TASK can access.
- **OS Interrupts Lock Time**: This is the ammount of time that a TASK/ISR2 can suspend OS Interrupts (with **SupendOSInterrupts**).
- **All Interrupts Lock Time**: This is the ammount of time that a TASK/ISR2 can suspend/disable All Interrupts (with **SupendAllInterrupts** **DisableAllInterrupts**).

**Autosar Timing Protection do NOT use OS-Application configuration but is done on schedulable entities (TASKs and ISR2).**

All timings are expressed in **Seconds**.

An example of **timing protection budgets** configuration:

```
 TASK Task1 {
   ...
   TIMING_PROTECTION = TRUE {
     EXECUTIONBUDGET         = 0.0025;
     MAXALLINTERRUPTLOCKTIME = 0.0001;
     RESOURCE = RESOURCELOCK {
       RESOURCELOCKTIME = 0.0002;
       RESOURCE = RES_SCHEDULER;
     };
     RESOURCE = RESOURCELOCK {
       RESOURCELOCKTIME = 0.0003;
       RESOURCE = RESOURCE1;
     };
   };
 };
 
 ISR ISR1 {
   CATEGORY = 2;
   ...
   TIMING_PROTECTION = TRUE {
     EXECUTIONTIME           = 0.0055;
     MAXALLINTERRUPTLOCKTIME = 0.0001;
   };
 };
```

Timing Protection, can be configured to protect from too frequents TASKs' activations and ISR2s' preemptions. This mechanism is called **inter-arrival** time protection.

An example of **inter-arrival time protection** configuration.

```
 TASK TaskPrio2 {
   ...
   TIMING_PROTECTION = TRUE {
     TIMEFRAME               = 0.00025;  /* Two Activation of this TASK have to be separated by 250us to be acceptated. (Provided that TASK's number activation is respected) */
     EXECUTIONBUDGET         = 0.0005;
     MAXALLINTERRUPTLOCKTIME = 0.0001;
   };
 };
 
 ISR Button_ISR2 {
   CATEGORY = 2;
   ... 
   TIMING_PROTECTION = TRUE {
     TIMEFRAME               = 0.001; /* Two interrupts of this type have to be separated by 1ms to be acceptated */
     EXECUTIONTIME           = 0.0055;
     MAXALLINTERRUPTLOCKTIME = 0.0001;
   };
 };
```

**N.B.** Check following examples:

- tricore/infineon\_TriBoard-TC2X5\_V2.0/Timing Protection automatic tests/Timing Protection budgets automatic tests
- tricore/infineon\_TriBoard-TC2X5\_V2.0/Timing Protection automatic tests/Timing Protection inter-arrival protection automatic tests

for configuration examples.

<a id="Stack_Monitoring"></a>

### Stack Monitoring

On processors that do not provide any memory protection hardware it may still be necessary to provide a “best effort with available resources” scheme for detectable classes of memory faults. Stack monitoring will identify where a task or ISR has exceeded a specified stack usage at context switch time.
This may mean that there is considerable time between the system being in error and that fault being detected. Similarly, the error may have been cleared at the point the fault is notified (the stack may be less than the specified size when the context switch occurs).
Note that if Memory Protection is enabled a stack overflow may cause a memory exception before the stack monitoring is able to detect the fault.

<a id="Architetures_that_support_full_AUTOSAR_Features"></a>

## Architetures that support full AUTOSAR Features

- [Infineon\_Aurix](Infineon_Aurix--2348.md "Infineon Aurix")

<a id="Note_on_Autosar_Scalabilty_Classes"></a>

## Note on Autosar Scalabilty Classes

**ERIKA's kernel now implement all the features specified in Autosar OS specification**, but do not support scalability classes yet.
Autosar Scalability Classes declare subsets of Autosar features and a set of checks that have to be done on configuration to guarantee that the subset is not overflowed. RT-Druid do not implement thsse checks (yet).

**Instead if a valid configuration is given to RT-Druid it enables all the features needed to support that configuration**.

---

## Archive provenance

- [Original page](http://erika.tuxfamily.org/wiki/index.php?title=Erika_AUTOSAR_OS) · [Archived source revision 6107](http://erika.tuxfamily.org/wiki/index.php?oldid=6107)
- Last source edit: 2018-05-07T15:07:57Z. Source retrieved on 2026-11-06; Markdown conversion completed on 2026-11-07.
- Original contributors recorded in exported history: Francesco, Eguidieri, Pj, Giuseppe Serano.
- [Original MediaWiki source](../source/wikitext/2476.mediawiki) · [Original editing history](../source/history/batch-004.xml)
- [Attribution and licensing notice](../NOTICE.md). Original file-specific notices, where present, remain applicable.
