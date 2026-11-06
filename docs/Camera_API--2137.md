# Camera API

The *mico32\_camera* component has some API functions distributed with a drive file *MicoCamera.h*.

<a id="Macros_in_MicoCamera.h_driver_file"></a>

### Macros in *MicoCamera.h* driver file

Macro used in *micro32\_camera's* API function:

- *MICO\_CAM\_IF\_FLAG\_MASK*
- *MICO\_CAM\_ERR\_FLAG\_MASK*
- *MICO\_CAM\_START\_MASK*
- *MICO\_CAM\_IFACK\_MASK*
- *MICO\_CAM\_RESET\_MASK*
- *MICO\_CAM\_ENABLE\_IRQ\_MASK*
- *MICO\_CAM\_IF\_FLAG\_CLEAR\_MASK*
- *MICO\_CAM\_SIZE\_MASK*

<a id="functions_in_MicoCamera.h_drivers_file"></a>

### functions in *MicoCamera.h* drivers file

This is the *micro32\_camera's* API function list (for more information on flags and registers please refer to [Mico32\_camera: Writing drivers based on mico32\_camera](Mico32_camera_Writing_drivers_based_on_mico32_camera--2069.md "Mico32 camera: Writing drivers based on mico32 camera")):

- *Mico\_camera\_write\_address(cam, address)*

For capture a image from CMOS camera the data must be stored a memory device from a base address. This function set the base address in the internal component register.

- *Mico\_camera\_read\_address(cam)*

It's possible read the register base address with this function.

- *Mico\_camera\_read\_status\_register(cam)*

The *mico32\_camera* switches in a finite number of states during its operation. The function returns the current state of component.

- *Mico\_camera\_read\_IF\_flag(cam)*

The function return the IF flag value. This function can be useful for waiting the end capture image in polling mode.

- *Mico\_camera\_read\_ERR\_flag(cam)*

During the operation image storage the component write on memory device by wishbone bus. Can happen a error access bus (for example wrong address) or an buffer fifo overflow. In these case the flag ERR is set. The function returns this value flag.

- *Mico\_camera\_start(cam)*

After call this function the component wait a new frame image. As it arrives is stored in the memory device (from address set by *Mico\_camera\_write\_address(cam, address)*).

- *Mico\_camera\_clear\_IRQ\_flag(cam)*

The component, if it properly set, can generate an interrupt after a image capture. In the handler interrupt must be called this function for clear the IRQ flag.

- *Mico\_camera\_reset(cam)*

Every time is called this api the component switches in RESET state and reset all its internal registers. After then first vsync signal by camera it cames in the IDLE state and waits the start capture image.

- *Mico\_camera\_enable\_IRQ(cam)*

By default the component works without use of interrupt request. After call this function at end of a image capture an interrupt is generated.

- *Mico\_camera\_disable\_IRQ(cam)*

Disable the interrupt request after than it has been previously activate.

- *Mico\_camera\_write\_divisor(cam, divisor)*

The CMOS camera is a digital logic than needs a source clock to work. The clock is provided by component *mico32\_camera*. The frequency value is set by this api than dived the platform frequency value by (2 / (divisor + 1)). Example with divisor = 3 the platform frequency is divided by 2. Divisor can't be set to zero value.

- *Mico\_camera\_read\_divisor(cam)*

Return the divisor value.

- *Mico\_camera\_frame\_terminated(cam)*

This function is identical to *Mico\_camera\_read\_IF\_flag(cam)*.

- *Mico\_camera\_size\_value(cam, value)*

This register should be set to the value of image size (in bytes). If we don't want the control image we write 0 (zero) value.

- *Mico\_camera\_size\_frame\_error(cam)*

If the image's size in bytes is different from the value register count, this bit is set.

<a id="Code_example_of_the_MicoCamera.h_API_Macros_and_functions"></a>

### Code example of the *MicoCamera.h* API Macros and functions

This is a simple C code that uses some API contained in the *MicoCamera.h* file:

```
#include <system_conf.h>
#include "MicoCamera.h"

/* Address were will be stored the data image. */
#define SDRAM_BASE_ADDRESS IMAGE_DATA_SDRAM

/* Image value. */
#define IMAGE_WIDTH    640
#define IMAGE_HEIGHT   480
#define IMAGE_BYTES_PER_PIXEL	1

/* 
   mico32_camera instantiation structure, 
   macro CAMERA_BASE_ADDRESS from system_conf.h file.
*/
MicoCamera_t* camera = (MicoCamera_t*)CAMERA_BASE_ADDRESS;

int main(void) {

   /* variable to storege state component. */
   unsigned long state;

   /* Set the camera by I2c with resolution 640x480 1 byte data. */
   // ...

   /* Reset the component mico32_camera (recommended) */
   Mico_camera_reset(camera);

   /* Waiting IDLE state (after reset component is in RESET state */
   do {

       /* Read component state */
       state = Mico_camera_read_status_register(camera);

       /* Timeout is a good idea */

   } while(state != MICO_CAMERA_IDLE);

   /* 
      With div_value = 3 and f = 50MHz,
      the mclk will be: (2 * 50) / (3 + 1) = 25MHz
   */
   Mico_camera_write_divisor(camera, 3);

   /* 
      Save the memory address were will be stored the data image in the internal
      component register.
   */
   Mico_camera_write_address(camera, (void*)IMAGE_DATA_SDRAM);
  
   /* Start a new image acquisition */
   Mico_camera_start(camera);	

   /* At end of the image acquisition the component return in the IDLE state */
   do {

       /* Read component state */
       state = Mico_camera_read_status_register(camera);

       /* Timeout is a good idea */

   } while(state != MICO_CAMERA_IDLE);

   /* 
      The image is stored in the memory device.
      Now we can put it on the uart port.
   */
   send_image((unsigned char*)IMAGE_DATA_SDRAM, IMAGE_WIDTH, IMAGE_HEIGHT);

   return 0;
}

/* Print on Uart the image data as PGM file. */
void send_image(volatile unsigned char* pun, unsigned int width, unsigned int height)
{
   unsigned i, j;

   /* Print the header of pgm file */ 
   printf("P2\r\n"
       "%d %d \r\n"
       "255\r\n", width, height);

   /* Print out the image data */
   for (i = 0; i < height; i++) {

       for (j = 0; j < width; j++) {

           printf("%d ", *pun);

           pun += IMAGE_BYTES_PER_PIXEL;

       }

   printf("\r\n");

   }

}
```

---

## Archive provenance

- [Original page](http://erika.tuxfamily.org/wiki/index.php?title=Camera_API) · [Archived source revision 3880](http://erika.tuxfamily.org/wiki/index.php?oldid=3880)
- Last source edit: 2011-10-17T12:17:54Z. Source retrieved on 2026-11-06; Markdown conversion completed on 2026-11-07.
- Original contributors recorded in exported history: Salva.
- [Original MediaWiki source](../source/wikitext/2137.mediawiki) · [Original editing history](../source/history/batch-002.xml)
- [Attribution and licensing notice](../NOTICE.md). Original file-specific notices, where present, remain applicable.
