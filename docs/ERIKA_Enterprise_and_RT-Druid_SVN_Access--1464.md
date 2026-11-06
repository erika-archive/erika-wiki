# ERIKA Enterprise and RT-Druid SVN Access

<a id="Anonymous.2C_readonly_access"></a>

### Anonymous, readonly access

- ERIKA Enterprise
  - SVN anonymous access: <svn://svn.tuxfamily.org/svnroot/erika/erikae/repos/ee/trunk/ee>
  - [web access to the SVN repository](http://svn.tuxfamily.org/viewvc.cgi/erika_erikae/repos/ee/trunk/ee)

- RT-Druid
  - SVN anonymous access: <svn://svn.tuxfamily.org/svnroot/erika/erikae/repos/rtdruid/trunk/rtdruid>
  - [web access to the SVN repository](http://svn.tuxfamily.org/viewvc.cgi/erika_erikae/repos/rtdruid/trunk/rtdruid/)

- Scicos-FLEX
  - SVN anonymous access: <svn://svn.tuxfamily.org/svnroot/erika/erikae/repos/scilab_codegen/trunk/>
  - [web access to the SVN repository](http://svn.tuxfamily.org/viewvc.cgi/erika_erikae/repos/scilab_codegen/trunk/)

- Latex Manuals
  - SVN anonymous access: <svn://svn.tuxfamily.org/svnroot/erika/erikae/repos/manuals/trunk/manuals>
  - [web access to the SVN repository](http://svn.tuxfamily.org/viewvc.cgi/erika_erikae/repos/manuals/trunk/manuals)

---



---

(for manuals and other erika related code see the URLs in "Authenticated access" below (just removing '+ssh' and the 'username@'))

<a id="Authenticated.2C_readwrite_access"></a>

### Authenticated, readwrite access

<a id="Gaining_access"></a>

#### Gaining access

Two steps are needed to have a TUXFAMILY\_USERNAME usable to edit the files in the Erika:

- [Subscribe](https://panel.tuxfamily.org/subscribe.pl) to Tuxfamily.

- Mail to the administrator (pj \_AT\_ evidence.eu.com at the moment) asking to have the new username added in the erika project.

<a id="URLs"></a>

#### URLs

ERIKA Enterprise source code

- svn+ssh://TUXFAMILY\_USERNAME@svn.tuxfamily.org/svnroot/erika/erikae/repos/ee/trunk/ee

RT-Druid source code

- svn+ssh://TUXFAMILY\_USERNAME@svn.tuxfamily.org/svnroot/erika/erikae/repos/rtdruid/trunk/rtdruid

ERIKA and RT-Druid manuals source code

- svn+ssh://TUXFAMILY\_USERNAME@svn.tuxfamily.org/svnroot/erika/erikae/repos/manuals/trunk/manuals

Scicos-FLEX code generation

- svn+ssh://TUXFAMILY\_USERNAME@svn.tuxfamily.org/svnroot/erika/erikae/repos/scilab\_codegen/trunk/

Project root

- svn+ssh://svn.tuxfamily.org/svnroot/erika/erikae

<a id="post-commit_hook"></a>

### post-commit hook

It is possible to receive an email everytime that a commit is done on the ERIKA SVN repository.

<a id="How_to_subscribe.2Funsubscribe"></a>

#### How to subscribe/unsubscribe

From the [tuxfamily MailingList faq](http://faq.tuxfamily.org/MailingLists/En#How_to_use), declined with the erika post-commit hook mailing list:

> To subscribe to the erika post-commit hook mailinglist, just
>
> - send an email to erika-request\_AT\_lists.tuxfamily.org
> - with subject: "subscribe"

(yes, you read correctly, the -request is for administrative management). An email is sent back to confirm the request. To unsubscribe, it's the same thing but with the subject being "unsubscribe". And to annoy the user till the end, confirmation is needed too.

<a id="subscription_alternatives_.5Bnow_unsupported.5D"></a>

##### subscription alternatives [now unsupported]

The [french mailinglist faq](http://faq.tuxfamily.org/MailingLists/Fr#Inscription_.C3.A0_une_liste_via_un_formulaire) describes a webpage alternative to the "send email to subscribe" protocol.

<a id="Contained_information"></a>

#### Contained information

These mails contain:

- Revision number
- Author
- Date
- Commit message
- Modified paths
- Diff (in attachment)

The subject of the mails is in this form:

```
[erika] [Revision#] First-commit-msg-line
```

(Note: this is not correct. First-commit-msg-line is the first line, or the content of the first line until the first dot if there is any)

---

## Archive provenance

- [Original page](http://erika.tuxfamily.org/wiki/index.php?title=ERIKA_Enterprise_and_RT-Druid_SVN_Access) · [Archived source revision 4912](http://erika.tuxfamily.org/wiki/index.php?oldid=4912)
- Last source edit: 2012-11-05T09:11:47Z. Source retrieved on 2026-11-06; Markdown conversion completed on 2026-11-07.
- Original contributors recorded in exported history: Roberto, WikiSysop, Paolo.gai, Dibbe, Nicola.
- [Original MediaWiki source](../source/wikitext/1464.mediawiki) · [Original editing history](../source/history/batch-003.xml)
- [Attribution and licensing notice](../NOTICE.md). Original file-specific notices, where present, remain applicable.
