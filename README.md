Learn Python The Hard Way Study Projects
========================================

I'm developing a course that will teach basic systems programming to devops
people (or just anyone) and will be creating a set of projects for them to
complete.  In the process I've been developing the code and the problem set so
I decided to create a project that contains them.  There's also a similar
project by Lynn Root.

The purpose of this will be to take a devops or sysadmin who's just completed
my book "Learn Python The Hard Way" and get them to build basic systems tools
from nothing.  My research shows that many sysadmins are great at finding and
using tools, but not as good at building tools from nothing and this is
hindering their ability to find work.  With this set of projects you can get
a solid understanding of basic programming problem solving, building projects,
and also how many of the tools you use actually work.

There will also be a similar project for Ruby that has the same projects but
different code.

Current List Of Projects
========================

I'm still formulating the code and structure for these projects, but here's
my list so far:

1. A grep-like tool.
2. A log file summarizer.
4. An email sending command line tool.
4. A simple daemon that does nothing but daemonize properly.
5. A daemon that watches other daemons and sends an email when they go down.
6. A daemon that watches logs and emails when a trigger is hit.
7. A grep-like that easily searches directories.
8. A smart directory copy tool.
9. A daemon that watches a directory for changes.
10. A backup tool using Paramiko.
11. A backup tool using Boto to S3.
12. A directory diff tool.
13. A directory patch tool.
14. A basic ZeroMQ client/server.
15. A ZeroMQ server that records stats and events to a DB.
16. A daemon that watches /proc and notifies the #15 server of changes.
17. A basic client/server using plain sockets.
18. A port scanner using sockets.
19. A socket honey pot daemon.
20. A daemon that receives block requests over zeromq and blocks IP addresses with firewall rules.

If you have other suggestions then send me a pull request to this document.  The key
is to think, "What would really help a modern sysadmin understand and automate the hell
out of a unix box thus making Chef/Puppet/Ansible/Salt easier."  Another thought is,
"If I wanted to teach the devops who will eventually wipe out Nagios with something
better, what should they know."


