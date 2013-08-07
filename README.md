Learn Python The Hard Way Study Projects
========================================

The LPTHW Study Projects are a set of problems to teach new programmers
(or experienced ones) basic systems programming.  It does this by presenting
a set of problems that you solve before looking at the solution I've written.
By solving all of these problems you'll improve your Python skills, get better
at building software from nothing, and learn more about how the operating
system works.

The projects are designed to teach you something about the operating systems
you use everyday through Python's APIs and implementing small versions of 
tools you use.  Each project has a catchy title for what it teaches, and
a name of the tool it's based on.  The problem will then be described 
in terms of this problem, what you'll learn, and what this tool does.

The Projects
============

The projects are broken down into categories of things you will learn
and are meant to be done in order, although you can pick and choose if
you are already familiar with other subjects.


Filesystem
-----

* find: The file system is a dictionary not a tree.
* grep: Regex are not scary, scary regex are.
* cp: Copying files fast and slow.
* mv: A move is a rename in the filesystem dictionary.
* rm: A remove deletes from the dictionary.
* tail: A file is like a tape drive.
* diff: A delta is a glorious thing.

Daemons
-------

* config: Don't invent your own config file format.
* logging: You don't need syslog.
* syslog: You should centralize logs with syslog.
* fork: Daemons are your friends.
* chroot: Daemons need cages.
* droppriv: Daemons can't be trusted.
* signals: Daemons can be poked.
* pidfiles: Daemons can bet lost.
* monit: Daemons need a nanny.
* watcher: A Daemon that's a tattle tail.

Network
-------

* mail: Sending email is easy.
* sendmail: Sometimes email should dump to your screen.
* curl: Getting things from the web.
* webserver: Everyone can make a web framework!
* ssh: Logging into servers is best securely.
* scp: Copying to another machine (even slower).
* s3: Copying to the cloud.
* named pipe: Everything is a file (except when it's not).
* sockets: A socket is a file (except when it's not).
* gevent: Sockets do a lot of nothing most of the time.

Security
--------

* iptables: Blocking ninja network haxors.
* blocker: Daemons can do the blocking.
* nmap: Scanning ports is easy and fun.
* honeypot: Scanning should not be easy.

System Info
-----------

* /proc: Daemons watching proc watching daemons.
* login: Watching logins and failures.
* /etc/passwd: Getting the dirt on users.
* stats: Good stats made easy with one file.
* nagios: Watching what is going on everywhere.


The Solutions
=============

Each project includes the solutions in a separate directory so you 
can compare your solution to mine and see how I'd have done it.
This also lets you study on your own since, if you get stuck, you
can cheat real quick and get back on track.


The Template
============

Every problem is written out in a consistent way with the following
information:


Title
-----

Synopsis of the project and what it teaches you.

Setup
-----

Required setup to complete the project including required reading and
what the student needs to install to complete the project successfully.


Problem
-------

Complete description of the problem to solve.


Requirements
------------

Required elements to the solution to meet the learning objectives.


Hints
-----

Any small hints or clues that tell them how to spot if they're doing it
wrong.

Assessment
----------

Tests and extra checks to confirm they did it right.

Deep Dive
---------

A list of code files in projects they should read to understand
what is going on.  No more assuming it works until they know it
works.


Other Languages
===============

I will be writing a Ruby version of this project to mirror the same
programs and will license this project so that other languages can
redo it in their language.


