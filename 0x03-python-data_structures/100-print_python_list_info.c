#include <stdio.h>
#include <python.h>

/**
 * print_python_list_info - This is a function that print the python info
 * @p: pointer
 * Return: nothing
 */

void print_python_list_info(PyObject *p)
{
	int size, alloc, i;
	PyObject *obj;

	size = Py_SIZE(p);
	alloc = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", alloc);

	for (i = 0; i < size; i++)
	{
		printf("Element %d: ", i);

		obj = PyList_GetItem(p, i);
		printf("%s\n", Py_TYPE(obj)->tp_name);
	}
}
