#!/bin/sh
# Example for use of GNU gettext.
# This file is in the public domain.
#
# Script for cleaning all autogenerated files.

test ! -f Makefile || make distclean
rm -rf autom4te.cache

# Brought in by explicit copy.
rm -f m4/nls.m4
rm -f m4/po.m4
rm -f m4/progtest.m4
rm -f po/remove-potcdate.sin

# Generated by aclocal.
rm -f aclocal.m4

# Generated by autoconf.
rm -f configure

# Generated or brought in by automake.
rm -f Makefile.in
rm -f m4/Makefile.in
rm -f po/Makefile.in
rm -f install-sh
rm -f missing
rm -f po/*.pot
rm -f po/stamp-po
rm -f po/*.gmo
