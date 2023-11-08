#include <Python.h>
#include <stdio.h>

void print_python_bytes(PyObject *p)
{
	char *str = PyBytes_AS_STRING(bytesObj);
	int i = 0;

	if (PyBytes_Check(p))
	{
		PyBytesObject *bytesObj = (PyBytesObject *)p;
		Py_ssize_t size = PyBytes_GET_SIZE(bytesObj);
		printf("[.] bytes object info\n");
		printf("  size: %zd\n", size);
		printf("  trying string: %s\n", str);
		printf("  first 10 bytes: ");
		for (i = 0; i < 10 && i < size; i++)
		{
			printf("%02x ", (unsigned char)str[i]);
		}
		printf("\n");
	}
	else
	{
		printf("[.] bytes object info\n");
		printf("  [ERROR] Invalid Bytes Object\n");
	}
}

void print_python_list(PyObject *p)
{
	Py_ssize_t i = 0;

	if (PyList_Check(p))
	{
		PyListObject *listObj = (PyListObject *)p;
		Py_ssize_t size = PyList_GET_SIZE(listObj);
		printf("[*] Python list info\n");
		printf("[*] Size of the Python List = %zd\n", size);
		printf("[*] Allocated = %zd\n", listObj->allocated);
		for (i = 0; i < size; i++)
		{
			PyObject *item = PyList_GET_ITEM(listObj, i);
			if (PyBytes_Check(item))
			{
				print_python_bytes(item);
			}
			else if (PyList_Check(item))
			{
				print_python_list(item);
			}
			else
			{
				printf("Element %zd: %s\n", i, Py_TYPE(item)->tp_name);
			}
		}
	}
	else
	{
		printf("[.] Python list info\n");
		printf("[ERROR] Invalid List Object\n");
	}
}

int main(void)
{
	Py_Initialize();
	PyObject *bytesObj = PyBytes_FromString("Hello");
	PyObject *listObj = PyList_New(2);
	PyList_SET_ITEM(listObj, 0, bytesObj);
	PyList_SET_ITEM(listObj, 1, bytesObj);
	print_python_bytes(bytesObj);
	print_python_list(listObj);
	Py_Finalize();
	return (0);
}
