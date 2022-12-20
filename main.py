from ulauncher.api.client.Extension import Extension
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.event import KeywordQueryEvent
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.action.OpenUrlAction import OpenUrlAction

class GCPLauncherExtension(Extension):

    def __init__(self):
        super(GCPLauncherExtension, self).__init__()
        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())

class KeywordQueryEventListener(EventListener):

    def on_event(self, event, extension):

        actions = list()
        query = event.get_argument() or ""

        array = [
            [
                "Dashboard",
                OpenUrlAction("https://console.cloud.google.com/home/dashboard?authuser=1"),
                "images/gcp_logo.png"
            ],
            [
                "Compute Engine",
                OpenUrlAction("https://console.cloud.google.com/compute?authuser=1"),
                "images/compute_icon.png"
            ],
            [
                "Kubernetes Engine",
                OpenUrlAction("https://console.cloud.google.com/kubernetes?authuser=1"),
                "images/kube_icon.png"
            ],
            [
                "Cloud SQL",
                OpenUrlAction("https://console.cloud.google.com/sql?authuser=1"),
                "images/sql_icon.png"
            ],
            [
                "App Engine",
                OpenUrlAction("https://console.cloud.google.com/appengine?authuser=1"),
                "images/app_engine_icon.png"
            ],
            [
                "Cloud Functions",
                OpenUrlAction("https://console.cloud.google.com/functions?authuser=1"),
                "images/cloud_functions_icon.png"
            ],
            [
                "Datastore",
                OpenUrlAction("https://console.cloud.google.com/datastore?authuser=1"),
                "images/datastore.png"
            ],
            [
                "BigQuery",
                OpenUrlAction("https://console.cloud.google.com/bigquery?authuser=1"),
                "images/big_query.png"
            ],
            [
                "Storage",
                OpenUrlAction("https://console.cloud.google.com/storage?authuser=1"),
                "images/storage_icon.png"
            ],
            [
                "VPC Network",
                OpenUrlAction("https://console.cloud.google.com/networking?authuser=1"),
                "images/vpc_network_icon.png"
            ],
            [
                "Network Services",
                OpenUrlAction("https://console.cloud.google.com/net-services?authuser=1"),
                "images/network_services_icon.png"
            ],
            [
                "Cloud Build",
                OpenUrlAction("https://console.cloud.google.com/cloud-build?authuser=1"),
                "images/build_icon.png"
            ],
            [
                "Container Registry",
                OpenUrlAction("https://console.cloud.google.com/gcr?authuser=1"),
                "images/container_registry_icon.png"
            ],
            [
                "Security",
                OpenUrlAction("https://console.cloud.google.com/security?authuser=1"),
                "images/security_icon.png"
            ],
            [
                "IAM Admin",
                OpenUrlAction("https://console.cloud.google.com/iam-admin?authuser=1"),
                "images/iam_admin_icon.png"
            ],
            [
                "Filestore",
                OpenUrlAction("https://console.cloud.google.com/filestore?authuser=1"),
                "images/filestore_icon.png"
            ],
            [
                "Stackdriver Logging",
                OpenUrlAction("https://console.cloud.google.com/logs?authuser=1"),
                "images/logging_icon.png"
            ],
            [
                "Stackdriver Monitoring",
                OpenUrlAction("https://console.cloud.google.com/monitoring?authuser=1"),
                "images/monitoring_icon.png"
            ],
            [
                "Billing",
                OpenUrlAction("https://console.cloud.google.com/billing?authuser=1"),
                "images/billing_icon.png"
            ],
            [
                "Marketplace",
                OpenUrlAction("https://console.cloud.google.com/marketplace?authuser=1"),
                "images/marketplace_icon.png"
            ],
            [
                "Pricing Calculator",
                OpenUrlAction("https://cloud.google.com/products/calculator?authuser=1"),
                "images/pricing_calculator_icon.png"
            ]
        ]

        if query != "":
           array = [x for x in array if query.lower() in x[0].lower()]

        for val in array:
            actions.append(
                ExtensionResultItem(name=val[0], on_enter=val[1], icon=val[2])
            )

        return RenderResultListAction(actions)

if __name__ == '__main__':
    GCPLauncherExtension().run()
