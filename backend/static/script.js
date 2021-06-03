/**
 * Copyright 2018, Google LLC
 * Licensed under the Apache License, Version 2.0 (the `License`);
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *    http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an `AS IS` BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

// [START gae_python38_log]
// [START gae_python3_log]
'use strict';

var waiting = false;
window.addEventListener('load', function () {

  var loader = document.getElementById("loader");
  loader.style.display = "none"

  var sub = document.getElementById("subs").addEventListener("click", async function () {
    var text = document.getElementById("laporantext").value;
    loader.style.display = "inline-block"
    document.getElementById("subs").style.display = "none"
    const formdata = { "text": text };

    if (waiting == false) {
      waiting = true;

      await fetch('infer', {
        method: "POST",
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(formdata)
      })
        .then(response => response.json())
        .then(data => {
          document.getElementById("resp").value = JSON.stringify(data, null, "\t")
          waiting = false;
          loader.style.display = "none"
          document.getElementById("subs").style.display = "inline-block"
        }
        )
    }

  });

});
// [END gae_python3_log]
// [END gae_python38_log]
