# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


def gatherLibs(spec):
    allLibs = ["iam","spanner","bigtable","bigquery","logging","pubsub","storage"]
    libs = {}
        
    for lib in allLibs:
        includeLib = "+" + lib
        excludeLib = "-" + lib
        if includeLib in spec:
            libs[lib] = True
        if excludeLib in spec and lib in libs:
            del libs[lib]

    return libs


class GoogleCloudCpp(CMakePackage):
    """C++ Client Libraries for Google Cloud Services"""

    homepage = "https://github.com/googleapis/google-cloud-cpp"
    url = "https://github.com/googleapis/google-cloud-cpp/archive/refs/tags/v2.28.0.tar.gz"
    git = "https://github.com/googleapis/google-cloud-cpp.git"
    
    maintainers("levinem")

    license("Apache-2.0", checked_by="levinem")

    version("develop", branch="develop")
    version("2.28.0", sha256="1d51910cb4419f6100d8b9df6bccd33477d09f50e378f12b06dae0f137ed7bc6")
    version("2.27.0", sha256="333fe00210ce1a6f0c1b51c232438a316eaf2c7a1724f75d0b2c64f8fc456aa7")
    version("2.26.0", sha256="91cd0552c68d85c0c07f9500771367034ea78f6814603275dcf8664472f8f37f")
    version("2.25.1", sha256="6e305a755798aad3f7ac1c7d9a660862d27bc7e8e5dfa041822af380a2f238a1")
    version("2.25.0", sha256="6f58213e2af16326392da84cd8a52af78cb80bc47338eb87e87d14c14c0e6bad")
    version("2.24.0", sha256="8d398958cad2338087ed5321db1d2c70a078d5d9d4dde720449395a3365a9ced")
    version("2.23.0", sha256="ce18fbd3a50170fb0c3d4cacf8a09136314f00136cdac99dad23b43de5d5bb62")
    version("2.22.0", sha256="0c68782e57959c82e0c81def805c01460a042c1aae0c2feee905acaa2a2dc9bf")
    version("2.21.0", sha256="b820159a4e6f17d0225e2266da563e53884567b8b33d00e45b30bc86be90ad1d")
    version("2.20.0", sha256="0f42208ca782249555aac06455b1669c17dfb31d6d8fa4baad29a90f295666bb")

    variant(
        "all",
        default=False,
        description="Compile all of the GA libraries",
    )

    variant(
        "shared",
        default=False,
        description="compile the libraries as shared libraries",
    )

    allLibs = ["iam","spanner","bigtable","bigquery","logging","pubsub","storage"]
    libs = {}
        
    for lib in allLibs:
        includeLib = "+" + lib
        excludeLib = "-" + lib
        with when(includeLib):
            libs[lib] = True
        with when(excludeLib):
            del libs[lib]

    for lib in libs:
        variant(lib, default=False, description=f"Compile the {lib} library")

    if len(libs) == 0 or (len(libs) == 1 and "storage" not in libs) or len(libs) > 1:
        depends_on("grpc")
        depends_on("protobuf")
        
    # @property
    # def libs(spec):
    #     allLibs = ["iam","spanner","bigtable","bigquery","logging","pubsub","storage"]
    #     returnLibs = {}
        
    #     for lib in allLibs:
    #         includeLib = "+" + lib
    #         excludeLib = "-" + lib
    #         if includeLib in spec:
    #             returnLibs[lib] = True
    #         if excludeLib in spec and lib in libs:
    #             del returnLibs[lib]
    #     return ",".join(list(returnLibs.keys()))
    # libs = gatherLibs(self.spec)

    # def generateLibraryVariants(self):
    #     libs = self.libs.split(",")
    #     for lib in libs:
    #         variant(lib, default=False, description=f"Compile the {lib} library")
    
    # variant(
    #     "iam",
    #     default=False,
    #     description="Compile the iam library",
    # )

    # variant(
    #     "spanner",
    #     default=False,
    #     description="Compile the spanner library",
    # )

    # variant(
    #     "bigtable",
    #     default=False,
    #     description="Compile the bigtable library",
    # )

    # variant(
    #     "bigquery",
    #     default=False,
    #     description="Compile the bigquery library",
    # )

    # variant(
    #     "logging",
    #     default=False,
    #     description="Compile the logging library",
    # )

    # variant(
    #     "pubsub",
    #     default=False,
    #     description="Compile the pubsub library",
    # )

    # variant(
    #     "storage",
    #     default=False,
    #     description="Compile the storage library",
    # )        


    
    generator("ninja")
    
    depends_on("ninja", type="build")
    depends_on("abseil-cpp")
    depends_on("curl")
    depends_on("google-crc32c")
    depends_on("openssl")
    depends_on("nlohmann-json")

    # def generateLibConditionalDependencies(self):
    #     libs = self.libs.split(",")
    #     if len(libs) == 0 or (len(libs) == 1 and "storage" not in libs) or len(libs) > 1:
    #         depends_on("grpc")
    #         depends_on("protobuf")

    def cmake_args(self):
        spec = self.spec
        args = [
            self.define("BUILD_TESTING", False),
            self.define("GOOGLE_CLOUD_CPP_ENABLE_EXAMPLES", False)
        ]

        if "+shared" in spec:
            args.append(self.define("BUILD_SHARED_LIBS", "ON"))

        if "+all" in spec:
            args.append(self.define("GOOGLE_CLOUD_CPP_ENABLE", "__ga_libraries__"))
        else:
            libs = gatherLibs(spec)
            # allLibs = ["iam","spanner","bigtable","bigquery","logging","pubsub","storage"]
            # libsDict = {}
        
            # for lib in allLibs:
            #     includeLib = "+" + lib
            #     excludeLib = "-" + lib
            #     if includeLib in spec:
            #         libsDict[lib] = True
            #     if excludeLib in spec and lib in libs:
            #         del libsDict[lib]
            # libs = ",".join(list(libsDict.keys()))
    
            # libs = {}
            # if self.spec.satisfies("+iam"):
            #     libs["iam"] = True
            # if self.spec.satisfies("-iam") and "iam" in libs:
            #     del libs["iam"]

            # if self.spec.satisfies("+spanner"):
            #     libs["spanner"] = True
            # if self.spec.satisfies("-spanner") and "spanner" in libs:
            #     del libs["spanner"]                

            # if self.spec.satisfies("+bigtable"):
            #     libs["bigtable"] = True
            # if self.spec.satisfies("-bigtable") and "bigtable" in libs:
            #     del libs["bigtable"]

            # if self.spec.satisfies("+bigquery"):
            #     libs["bigquery"] = True
            # if self.spec.satisfies("-bigquery") and "bigquery" in libs:
            #     del libs["bigquery"]

            # if self.spec.satisfies("+logging"):
            #     libs["logging"] = True
            # if self.spec.satisfies("-logging") and "logging" in libs:
            #     del libs["logging"]

            # if self.spec.satisfies("+pubsub"):
            #     libs["pubsub"] = True
            # if self.spec.satisfies("-pubsub") and "pubsub" in libs:
            #     del libs["pubsub"]

            # if self.spec.satisfies("+storage"):
            #     libs["storage"] = True
            # if self.spec.satisfies("-storage") and "storage" in libs:
            #     del libs["storage"]

            # if len(libs) == 0 or (len(libs) == 1 and "storage" not in libs) or len(libs) > 1:
            #     depends_on("grpc")
            #     depends_on("protobuf")
            # libs = gatherLibs(self)
            #libs = self.libs.split(",")
            if len(libs) > 0:
                args.append(self.define("GOOGLE_CLOUD_CPP_ENABLE", ",".join(list(libs.keys()))))

            # If no libs are specified and +all is not specified, then the default libraries will be compiled.  Please see the google-cloud-cpp website for more information on the latest default libraries that will be installed.
        
        return args
