
SRCDIR=../oslab/linux-0.11

all: test1
	(cd $(SRCDIR);git checkout)
	(cp ./include/unistd.h $(SRCDIR)/include/unistd.h)
	(cp ./include/linux/sys.h $(SRCDIR)/include/linux/sys.h)	
	(cp ./kernel/Makefile $(SRCDIR)/kernel/Makefile)
	(cp ./kernel/system_call.s $(SRCDIR)/kernel/system_call.s)
	(cp ./kernel/who.c $(SRCDIR)/kernel/who.c)
	(cd ../oslab/linux-0.11/;make all)
	(cd ../oslab/;./run)

test1:
	echo "cp test code to hdc.img"
	(cd ../oslab; sudo ./mount-hdc)
	(cp -r test ../oslab/hdc/usr/root)
	(cp ./include/unistd.h ../oslab/hdc/usr/include)
	(cp ./include/linux/sys.h ../oslab/hdc/usr/linux)
	(cd ../oslab; sudo umount hdc)
	
clean:
	(cd ../oslab/linux-0.11/;git checkout -- .;make clean)
	rm ../oslab/linux-0.11/kernel/who.c


