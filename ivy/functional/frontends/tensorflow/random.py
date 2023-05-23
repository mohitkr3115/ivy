import ivy
from ivy.functional.frontends.tensorflow.func_wrapper import to_ivy_arrays_and_back
from ivy.func_wrapper import with_unsupported_dtypes


@with_unsupported_dtypes(
    {"2.9.0 and below": ("int8", "int16", "unsigned")}, "tensorflow"
)
@to_ivy_arrays_and_back
def uniform(shape, minval=0, maxval=None, dtype=ivy.float32, seed=None, name=None):
    return ivy.random_uniform(
        shape=shape, low=minval, high=maxval, dtype=dtype, seed=seed
    )


@with_unsupported_dtypes(
    {"2.9.0 and below": ("int8", "int16", "int32", "int64", "unsigned")}, "tensorflow"
)
@to_ivy_arrays_and_back
def normal(shape, mean=0.0, stddev=1.0, dtype=ivy.float32, seed=None, name=None):
    return ivy.random_normal(mean=mean, std=stddev, shape=shape, dtype=dtype, seed=seed)


# implement random shuffle
@with_unsupported_dtypes(
    {"2.9.0 and below": ("int8", "int16", "in32", "int64", "unsigned")}, "tensorflow"
)
@to_ivy_arrays_and_back
def shuffle(value, axis=0, seed=None, name=None):
    return ivy.shuffle(value, axis, seed=seed)


@to_ivy_arrays_and_back
def stateless_uniform(
    shape, seed, minval=0, maxval=None, dtype=ivy.float32, name=None, alg="auto_select"
):
    return ivy.random_uniform(
        shape=shape, seed=seed[0] + seed[1], low=minval, high=maxval, dtype=dtype
    )


@with_unsupported_dtypes(
    {"2.9.0 and below": ("int8", "int16", "unsigned")}, "tensorflow"
)
@to_ivy_arrays_and_back
def poisson(shape, lam, dtype=ivy.float32, seed=None, name=None):
    return ivy.poisson(shape=shape, lam=lam, dtype=dtype, seed=seed)


@with_unsupported_dtypes(
    {"2.9.0 and below": ("int8", "int16", "unsigned")}, "tensorflow"
)
@to_ivy_arrays_and_back
def stateless_normal(
    shape, seed, mean=0.0, stddev=1.0, dtype=ivy.float32, name=None, alg="auto_select"
):
    return ivy.random_normal(
        mean=mean, std=stddev, shape=shape, dtype=dtype, seed=seed[0] + seed[1]
    )


@with_unsupported_dtypes(
    {"2.9.0 and below": ("int8", "int16", "unsigned")}, "tensorflow"
)
@to_ivy_arrays_and_back
def stateless_poisson(shape, seed, lam, dtype=ivy.int32, name=None):
    return ivy.poisson(shape=shape, lam=lam, dtype=dtype, seed=seed[0] + seed[1])


@to_ivy_arrays_and_back
def gamma(shape, alpha, beta=None, dtype=ivy.float32, seed=None, name=None):
    return ivy.gamma(alpha, beta, shape=shape, dtype=dtype, seed=seed)
