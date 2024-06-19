#!/usr/bin/env bats

#
# PACKAGES
#

@test "curl is installed" {
    run which curl
    [ "$status" -eq 0 ]
}
