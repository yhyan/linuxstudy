
SRCDIR=../oslab/linux-0.11

all: cptest
	(cd $(SRCDIR);git checkout)
	(cp ./include/linux/kernel.h $(SRCDIR)/include/linux/kernel.h)
	(cp ./init/main.c $(SRCDIR)/init/main.c)
	(cp ./kernel/exit.c $(SRCDIR)/kernel/exit.c)
	(cp ./kernel/fork.c $(SRCDIR)/kernel/fork.c)
	(cp ./kernel/printk.c $(SRCDIR)/kernel/printk.c)
	(cp ./kernel/sched.c $(SRCDIR)/kernel/sched.c)
	(cd ../oslab/linux-0.11/;make all)
	(cd ../oslab/;./run)

cptest:
	echo "cp test code to hdc.img"
	(cd ../oslab; sudo ./mount-hdc)
	(rm -r ../oslab/hdc/usr/root/test; cp -r test ../oslab/hdc/usr/root/test)
	(cd ../oslab; sudo umount hdc)

cplog:
	echo "cp log from hdc.img"
	(cd ../oslab; sudo ./mount-hdc)
	(cp ../oslab/hdc/var/process.log ./test/)
	(cd ../oslab; sudo umount hdc)

clean:
	(cd ../oslab/linux-0.11/;git checkout -- .;make clean)


