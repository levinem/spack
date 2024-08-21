from spack.package import *

class GoogleCloudCpp(CMakePackage):
    """C++ Client Libraries for Google Cloud Services"""

    homepage = "https://github.com/googleapis/google-cloud-cpp"
    url = "https://github.com/googleapis/google-cloud-cpp/archive/refs/tags/v2.28.0.tar.gz"
    git = "https://github.com/googleapis/google-cloud-cpp.git"

    license("Apache-2.0")

    version("develop", branch="develop")
    version("2.28.0", )
