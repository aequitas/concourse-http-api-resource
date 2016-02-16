# HTTP API Resource

Concourse resource to allow interaction with (simple) HTTP API's.

https://hub.docker.com/r/aequitas/http-api-resource/

## Source Configuration

Most of the `source` options can also be used in `params` for the specifc actions. This allows to use a different URL path. For example when a POST and GET use different endpoints.

Options set in `params` take precedence over options in `source`.

* `uri`: *Required.* The URI to use for the requests.
    Example: `https://www.hipchat.com/v2/room/1234321/notification`

* `method`: *Optional* Method to use, eg: GET, POST, PATCH (default `GET`).

* `headers`: *Optional* Object containing headers to pass to the request.
    Example:

        headers:
            X-Some-Header: some header content

* `json`: *Optional* JSON to send along with the request.

* `debug`: *Optional* Set debug logging of scripts, takes boolean (default `false`).

## Behavior

Currently the only useful action the resource supports is `out`. The actions `in` and `check` will be added later.

### Interpolation

All options support interpolation of variables by using [Python string formatting](https://docs.python.org/3.5/library/stdtypes.html#str.format)

In short it means variables can be used by using single curly brackets (instead of double for Concourse interpolation). Eg: `Build nr. {BUILD_NAME} passed.`

Build metadata (BUILD_NAME, BUILD_JOB_NAME, BUILD_PIPELINE_NAME and BUILD_ID) are available as well as the merged `source`/`params` objects. Interpolation will happen after merging the two objects.

See Hipchat below for usage example.

## Examples

### Post notification on HipChat

This example show use of variable interpolation with build metadata and the params dict.

Also shows how the usage of a authentication header using Concourse variables.


```yaml
resources:
    - name: hipchat
      type: http-api
      source:
          uri: https://www.hipchat.com/v2/room/team_room/notification
          method: POST
          headers:
              Authorization: Bearer {hipchat_token}
          json:
              color: {color}
              message: Build {BUILD_PIPELINE_NAME}{BUILD_JOB_NAME}, nr: {BUILD_NAME} {message}!
          hipchat_token: {{HIPCHAT_TOKEN}}

jobs:
    - name: Test and notify
      plan:
          - task: build
            file: ci/build.yaml
            on_success:
                put: hipchat
                params:
                    color: green
                    message: was a success
            on_failure:
                put: hipchat
                params:
                    color: red
                    message: failed horribly

```
