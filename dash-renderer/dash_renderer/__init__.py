import sys

__file__
__version__ = "1.4.0"

_js_dist_dependencies = [
    {
        "external_url": {
            "prod": [
                "https://cdn.staticfile.org/babel-polyfill/7.8.7/polyfill.min.js",
                "https://cdn.staticfile.org/react/16.13.0/umd/react.production.min.js",
                "https://cdn.staticfile.org/react-dom/16.13.0/umd/react-dom.production.min.js",
                "https://cdn.staticfile.org/prop-types/15.7.2/prop-types.min.js",
            ],
            "dev": [
                "https://cdn.staticfile.org/babel-polyfill/7.8.7/polyfill.js",
                "https://cdn.staticfile.org/react/16.13.0/umd/react.development.js",
                "https://cdn.staticfile.org/react-dom/16.13.0/umd/react-dom.development.js",
                "https://cdn.staticfile.org/prop-types/15.7.2/prop-types.js",
            ],
        },
        "relative_package_path": {
            "prod": [
                "polyfill@7.8.7.min.js",
                "react@16.13.0.min.js",
                "react-dom@16.13.0.min.js",
                "prop-types@15.7.2.min.js",
            ],
            "dev": [
                "polyfill@7.8.7.min.js",
                "react@16.13.0.js",
                "react-dom@16.13.0.js",
                "prop-types@15.7.2.js",
            ],
        },
        "namespace": "dash_renderer",
    }
]


_js_dist = [
    {
        "relative_package_path": "{}.min.js".format(__name__),
        "dev_package_path": "{}.dev.js".format(__name__),
        "external_url": "https://flarekit-pkg.o3cloud.cn/dash-renderer@1.4.0"
        "/dash_renderer/dash_renderer.min.js",
        "namespace": "dash_renderer",
    },
    {
        "relative_package_path": "{}.min.js.map".format(__name__),
        "dev_package_path": "{}.dev.js.map".format(__name__),
        "namespace": "dash_renderer",
        "dynamic": True,
    },
]
