--- a/kivy/graphics/cgl_backend/cgl_mock.pyx
+++ b/kivy/graphics/cgl_backend/cgl_mock.pyx
@@
-cdef void mockUniform4f(GLint location, GLfloat v0, GLfloat v1, GLfloat v2, GLfloat v3):
+cdef void mockUniform4f(GLint location, GLfloat v0, GLfloat v1, GLfloat v2, GLfloat v3) nogil:
     # implementation…
     return

@@
-cdef void mockUniformMatrix4fv(GLint location, GLsizei count, GLboolean transpose, GLfloat* value):
+cdef void mockUniformMatrix4fv(GLint location, GLsizei count, GLboolean transpose, GLfloat* value) nogil:
     # implementation…
     return

@@
-cdef void mockUniform1i(GLint location, GLint v0):
+cdef int mockUniform1i(GLint location, GLint v0) nogil:
     # implementation…
-    return
+    return 0  # success
