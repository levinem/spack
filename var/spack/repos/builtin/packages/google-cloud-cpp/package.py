# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


def gatherLibs(spec):
    allLibs = [
        "accessapproval",
        "accesscontextmanager",
        "advisorynotifications",
        "aiplatform",
        "alloydb",
        "apigateway",
        "apigeeconnect",
        "apikeys",
        "appengine",
        "apphub",
        "artifactregistry",
        "asset",
        "assuredworkloads",
        "automl",
        "backupdr",
        "bigquery",
        "bigtable",        
        "billing",
        "certificatemanager",
        "commerce",
        "composer",
        "compute",
        "config",
        "connectors",
        "datastore",
        "deploy",
        "filestore",
        "functions",
        "grpc_utils",
        "iam",
        "iap",
        "ids",
        "kms",
        "language",
        "logging",
        "memcache",
        "monitoring",
        "netapp",
        "networkconnectivity",
        "networkmanagement",
        "networksecurity",
        "networkservices",
        "notebooks",
        "oath2",
        "opentelemetry",
        "optimization",
        "orgpolicy",
        "osconfig",
        "privateca",
        "profiler",
        "publicca",
        "pubsub",
        "pubsublite",
        "recommender",
        "redis",
        "retail",
        "run",
        "scheduler",
        "servicecontrol",
        "servicehealth",
        "serviceusage",
        "shell",
        "spanner",
        "sql",
        "storage",
        "support",
        "talent",
        "tasks",
        "texttospeech",
        "tpu",
        "trace",
        "translate",
        "video",
        "vision",
        "vpcaccess",
        "webrisk",
        "workflows",
        "workstations"
    ]
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

    allLibs = [
        "accessapproval",
        "accesscontextmanager",
        "advisorynotifications",
        "aiplatform",
        "alloydb",
        "apigateway",
        "apigeeconnect",
        "apikeys",
        "appengine",
        "apphub",
        "artifactregistry",
        "asset",
        "assuredworkloads",
        "automl",
        "backupdr",
        "bigquery",
        "bigtable",        
        "billing",
        "certificatemanager",
        "commerce",
        "composer",
        "compute",
        "config",
        "connectors",
        "datastore",
        "deploy",
        "filestore",
        "functions",
        "grpc_utils",
        "iam",
        "iap",
        "ids",
        "kms",
        "language",
        "logging",
        "memcache",
        "monitoring",
        "netapp",
        "networkconnectivity",
        "networkmanagement",
        "networksecurity",
        "networkservices",
        "notebooks",
        "oath2",
        "opentelemetry",
        "optimization",
        "orgpolicy",
        "osconfig",
        "privateca",
        "profiler",
        "publicca",
        "pubsub",
        "pubsublite",
        "recommender",
        "redis",
        "retail",
        "run",
        "scheduler",
        "servicecontrol",
        "servicehealth",
        "serviceusage",
        "shell",
        "spanner",
        "sql",
        "storage",
        "support",
        "talent",
        "tasks",
        "texttospeech",
        "tpu",
        "trace",
        "translate",
        "video",
        "vision",
        "vpcaccess",
        "webrisk",
        "workflows",
        "workstations"
    ]    
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
        
    generator("ninja")
    
    depends_on("ninja", type="build")
    depends_on("abseil-cpp")
    depends_on("curl")
    depends_on("google-crc32c")
    depends_on("openssl")
    depends_on("nlohmann-json")

    def setup_run_environment(self, env):
        env.prepend_path("CMAKE_PREFIX_PATH", self.prefix)        
    
    def cmake_args(self):
        spec = self.spec
        args = [
            self.define("BUILD_TESTING", False),
            self.define("GOOGLE_CLOUD_CPP_ENABLE_EXAMPLES", False),
            self.define("GOOGLE_CLOUD_CPP_WITH_MOCKS", False)
        ]

        if "+shared" in spec:
            args.append(self.define("BUILD_SHARED_LIBS", "ON"))

        if "+all" in spec:
            args.append(self.define("GOOGLE_CLOUD_CPP_ENABLE", "__ga_libraries__"))
        else:
            libs = gatherLibs(spec)

            if len(libs) > 0:
                args.append(self.define("GOOGLE_CLOUD_CPP_ENABLE", ",".join(list(libs.keys()))))

            # If no libs are specified and +all is not specified, then the default libraries will be compiled.  Please see the google-cloud-cpp website for more information on the latest default libraries that will be installed.
        
        return args

