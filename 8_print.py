
id = 5
name = "Guido"
pi = 3.141529

#! 1 - print params
print("id=", id, "name=", name)

#! 2 Python inherits C format
print("id=[%05d], name=[%-10s], pi = [%10.2f]"%(id, name, pi))

#! 3 Python string.format() like c#
print("id={}, name={}".format(id,name))
print("id=[{0:010}], name={1:10s}, pi=[{2:0.2f}]".format(id,name, pi))

#! 4 String interpolation
#$ Alignments of the string
print(f"id={id:010}, name=[{name:<10}]")
print(f"id={id:010}, name=[{name:>10}]")
print(f"id=[{id:p^10}], name=[{name:^10}]")
print(f"pi={pi:.3f}")
#$ Multiline
print(f"id={id},\n"
f"name=\t{name},"
f"pi={pi}")



#? Look for Format specifiers
