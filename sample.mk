

target2: target2 target3
	@echo "hello"


target3: target2 target3
	# hello
	@echo "hello"

# hello

a = 1
b=2
c=$(a) $(b)
d=$(d $(z))
target1: target2 target3
target12: target2 target3
	@echo "hello"

target12: target2 target3
	@echo "hello"

ifeq ($(UNAME), x86_64)
    a = 3
endif
ifeq ($(UNAME), x86_64)
    b=3
else
	c=4
endif
