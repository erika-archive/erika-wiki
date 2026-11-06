# Attaching a Servo motor to the EasyLab

Currently the PWM Block for the EasyLab board has a limited support in frequencies, making it impossible to have the 50Hz PWM needed to control a servo.

As a workaround, it is possible to do the following (hint provided by Chin Luh from Tritytech):

1. hardcode the 50 in easylab\_pwm.c
2. change P1TCONbits.PTCKPS = 0b11; and EE\_UINT16 ptper = EE\_get\_peripheral\_clock() / pwm\_freq / 64; in ee\_pwm.c.
3. resulting input vs. degree:
   1. 0.025  : 0 degree
   2. 0.0725 : 90 degree
   3. 0.12  : 180 degree

---

## Archive provenance

- [Original page](http://erika.tuxfamily.org/wiki/index.php?title=Attaching_a_Servo_motor_to_the_EasyLab) · [Archived source revision 5830](http://erika.tuxfamily.org/wiki/index.php?oldid=5830)
- Last source edit: 2014-09-18T09:40:41Z. Source retrieved on 2026-11-06; Markdown conversion completed on 2026-11-07.
- Original contributors recorded in exported history: Pj.
- [Original MediaWiki source](../source/wikitext/2481.mediawiki) · [Original editing history](../source/history/batch-002.xml)
- [Attribution and licensing notice](../NOTICE.md). Original file-specific notices, where present, remain applicable.
