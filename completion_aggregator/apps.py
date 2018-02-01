# -*- coding: utf-8 -*-
"""
completion_aggregator Django application initialization.
"""

from __future__ import absolute_import, unicode_literals

from django.apps import AppConfig


class CompletionAggregatorAppConfig(AppConfig):
    """
    Configuration for the completion_aggregator Django application.
    """

    name = 'completion_aggregator'
    plugin_app = {
        'url_config': {
            'lms.djangoapp': {
                'namespace': 'completion_aggregator',
                'regex': r'^completion-aggregator/',
                'relative_path': 'completion_aggregator.urls',
            },
        },
        'settings_config': {
            'lms.djangoapp': {
                'aws': {'relative_path': 'settings.aws'},
                'common': {'relative_path': 'settings.common'},
            },
        },
    }

    def ready(self):
        """
        Load signal handlers when the app is ready.
        """
        from . import signals as _