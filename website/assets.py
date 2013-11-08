# -*- coding: utf-8 -*-
import logging

from webassets import Environment, Bundle
from webassets.filter import get_filter

from website import settings

logger = logging.getLogger(__name__)

env = Environment(settings.STATIC_FOLDER, settings.STATIC_URL_PATH)

css = Bundle(
        # Vendorized libraries
         Bundle(
            "vendor/jquery-ui/css/jquery-ui.css",
            "vendor/jquery-tagit/css/jquery.tagit.css",
            "vendor/jquery-tagsinput/css/jquery.tagsinput.css",
            "vendor/jquery-tagit/css/tagit.ui-zendesk.css",
            "vendor/jquery-treeview/jquery.treeview.css",
            "vendor/jquery-fileupload/css/jquery.fileupload-ui.css",
            "vendor/pygments.css",
            "vendor/bootstrap3-editable/css/bootstrap-editable.css",
            "vendor/bootstrap3/css/bootstrap-theme.css",
            filters="cssmin"),
        # Site-specific CSS
        Bundle(
            "css/site.css",
            filters="cssmin"),
        output="public/css/common.css"
)


js = Bundle(
        # Vendorized libraries that are already minified
        Bundle(
                "vendor/jquery/jquery.min.js",
                "vendor/jquery-ui/js/jquery-ui.min.js",
                "vendor/bootstrap3/js/bootstrap.min.js",
                "vendor/bootstrap3-editable/js/bootstrap-editable.min.js",
                "vendor/bootbox/bootbox.min.js",
                "vendor/jquery-tagsinput/js/jquery.tagsinput.min.js",
                "vendor/jquery-tagcloud/jquery.tagcloud.js",
                "vendor/jquery-treeview/jquery.treeview.js",
                "vendor/jquery-tagit/js/tag-it.js",
                "vendor/knockout/knockout-min.js",
                "vendor/moment/moment.min.js"),
        # Site-specific JS
        Bundle("js/site.js", "js/project.js", "js/app.js", filters="jsmin"),
        output="public/js/common.js"
)


logger.debug("Registering asset bundles")
env.register("js", js)
env.register("css", css)
# Don't bundle in debug mode
env.debug = settings.DEBUG_MODE