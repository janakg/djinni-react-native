# AUTOGENERATED FILE - DO NOT MODIFY!
# This file generated by Djinni from enum.djinni

from djinni.support import MultiSet # default imported in all files
from djinni.exception import CPyException # default imported in all files
from djinni.pycffi_marshal import CPyEnum, CPyObject, CPyObjectProxy
from PyCFFIlib_cffi import ffi, lib

from djinni import exception # this forces run of __init__.py which gives cpp option to call back into py to create exception

class MapEnumColorEnumColorHelper:
    c_data_set = MultiSet()

    @staticmethod
    def check_c_data_set_empty():
        assert len(MapEnumColorEnumColorHelper.c_data_set) == 0
        Color.check_c_data_set_empty()
        Color.check_c_data_set_empty()

    @ffi.callback("int(struct DjinniObjectHandle *, int)")
    def __get_value(cself, key):
        pyKey = CPyEnum.toPy(Color, key)
        assert pyKey is not None
        try:
            _ret= CPyEnum.fromPy(CPyObjectProxy.toPyObj(None, cself)[pyKey])
            assert _ret.value != -1
            return _ret
        except Exception as _djinni_py_e:
            CPyException.setExceptionFromPy(_djinni_py_e)
            return ffi.NULL

    @ffi.callback("size_t(struct DjinniObjectHandle *)")
    def __get_size(cself):
        return len(CPyObjectProxy.toPyObj(None, cself))

    @ffi.callback("struct DjinniObjectHandle *()")
    def __python_create():
        c_ptr = ffi.new_handle(MapEnumColorEnumColorProxy(dict()))
        MapEnumColorEnumColorHelper.c_data_set.add(c_ptr)
        return ffi.cast("struct DjinniObjectHandle *", c_ptr)

    @ffi.callback("void(struct DjinniObjectHandle *, int, int)")
    def __python_add(cself, key, value):
        CPyObjectProxy.toPyObj(None, cself)[CPyEnum.toPy(Color, key)] = CPyEnum.toPy(Color, value)

    @ffi.callback("void(struct DjinniObjectHandle * )")
    def __delete(c_ptr):
        assert c_ptr in MapEnumColorEnumColorHelper.c_data_set
        MapEnumColorEnumColorHelper.c_data_set.remove(c_ptr)

    @ffi.callback("int(struct DjinniObjectHandle *)")
    def __python_next(cself):
        try:
            _ret= CPyEnum.fromPy(next(CPyObjectProxy.toPyIter(cself)))
            assert _ret.value != -1
            return _ret
        except Exception as _djinni_py_e:
            CPyException.setExceptionFromPy(_djinni_py_e)
            return ffi.NULL

    @staticmethod
    def _add_callbacks():
        lib.map_enum_color_enum_color_add_callback__get_value(MapEnumColorEnumColorHelper.__get_value)
        lib.map_enum_color_enum_color_add_callback___delete(MapEnumColorEnumColorHelper.__delete)
        lib.map_enum_color_enum_color_add_callback__get_size(MapEnumColorEnumColorHelper.__get_size)
        lib.map_enum_color_enum_color_add_callback__python_create(MapEnumColorEnumColorHelper.__python_create)
        lib.map_enum_color_enum_color_add_callback__python_add(MapEnumColorEnumColorHelper.__python_add)
        lib.map_enum_color_enum_color_add_callback__python_next(MapEnumColorEnumColorHelper.__python_next)

MapEnumColorEnumColorHelper._add_callbacks()

class MapEnumColorEnumColorProxy:
    def iter(d):
        for k in d:
            yield k

    def __init__(self, py_obj):
        self._py_obj = py_obj
        if py_obj is not None:
            self._py_iter = iter(py_obj)
        else:
            self._py_iter = None