from spack.package import *

class GoogleCloudCpp(CMakePackage):
    """C++ Client Libraries for Google Cloud Services"""

    homepage = "https://github.com/googleapis/google-cloud-cpp"
    git = "https://github.com/googleapis/google-cloud-cpp"

    license("Apache-2.0")

    version("main", branch="main")
