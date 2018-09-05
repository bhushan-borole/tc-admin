# -*- coding: utf-8 -*-

# This Source Code Form is subject to the terms of the Mozilla Public License,
# v. 2.0. If a copy of the MPL was not distributed with this file, You can
# obtain one at http://mozilla.org/MPL/2.0/.

import pytest

import ciadmin.check


@pytest.fixture(scope="session")
def generated():
    """Return the generated resources"""
    # this is set as a module-global before running the tests
    return ciadmin.check.generated


@pytest.fixture(scope="session")
def actual():
    """Return the actual resources (as fetched from Taskcluster)"""
    # this is set as a module-global before running the tests
    return ciadmin.check.actual