# flake8: NOQA
# "flake8: NOQA" to suppress warning "H104  File contains nothing but comments"
import cupy

# def c_
# class c_(object):
class CClass():
    def __getitem__(self, tup):
        """Joins arrays from an axis 1.

        Args:
            tup (sequence of arrays): Arrays to be joined. All of these should have
                same dimensionalities except the specified axis.

        Returns:
            cupy.ndarray: Joined array.

        .. seealso:: :func:`numpy.concatenate`

        """
        return cupy.concatenate(tup, axis=1)

# class r_(object):
class RClass():
    def __getitem__(self, tup):
        # def r_(tup):
        """Joins arrays from an axis 0.

        Args:
            tup (sequence of arrays): Arrays to be joined. All of these should have
                same dimensionalities except the specified axis.
            axis (int): The axis to join arrays along.

        Returns:
            cupy.ndarray: Joined array.

        .. seealso:: :func:`numpy.concatenate`

        """
        return cupy.concatenate(tup, axis=0)

c_ = CClass()
r_ = RClass()

def hangai(a=0):
    return True

# class s_(object):


# TODO(okuta): Implement indices


# TODO(okuta): Implement ix_


# TODO(okuta): Implement ravel_multi_index


# TODO(okuta): Implement unravel_index


# TODO(okuta): Implement diag_indices


# TODO(okuta): Implement diag_indices_from


# TODO(okuta): Implement mask_indices


# TODO(okuta): Implement tril_indices


# TODO(okuta): Implement tril_indices_from


# TODO(okuta): Implement triu_indices


# TODO(okuta): Implement triu_indices_from
