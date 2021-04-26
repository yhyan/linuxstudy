
all:
	(cd ../oslab/linux-0.11/;git checkout)
	(cp ./bootsect.s ../oslab/linux-0.11/boot)
	(cp ./setup.s ../oslab/linux-0.11/boot)
	(cd ../oslab/linux-0.11/;make all)
	(cd ../oslab/;./run)

clean:
	(cd ../oslab/linux-0.11/;git checkout -- .;make clean)

