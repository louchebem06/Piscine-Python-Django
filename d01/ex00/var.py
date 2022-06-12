#!/usr/local/bin/python3

def my_var():
	i = 42
	s = "42"
	s42 = "quarante-deux"
	f = 42.0
	b = True
	l = [42]
	d = {42: 42}
	t = (42,)
	se = set()
	print_base = "{0} has a type {1}"
	print(print_base.format(i, type(i)))
	print(print_base.format(s, type(s)))
	print(print_base.format(s42, type(s42)))
	print(print_base.format(f, type(f)))
	print(print_base.format(b, type(b)))
	print(print_base.format(l, type(l)))
	print(print_base.format(d, type(d)))
	print(print_base.format(t, type(t)))
	print(print_base.format(se, type(se)))

if __name__ == '__main__':
	my_var()