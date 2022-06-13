/**
 * IndexController.js
 *
 * @file  The Index Controller
 * @author Tomás Sánchez
 * @since  06.12.2022
 */

const API_URL = "https://www.dolarsi.com/api/api.php?type=valoresprincipales";

class Dollar {
  constructor(b = "--", s = "--") {
    this.buy = b;
    this.sell = s;
  }
}

(function IndexController() {
  getDollar();
})();

function getDollar() {
  fetch(API_URL)
    .then((data) =>
      data
        .json()
        .then((result) => {
          updateDollar(result.map((x) => x.casa));
        })
        .catch((e) => console.error(e))
    )
    .catch((e) => console.error(e));
}

/**
 * Updates Dollar Data.
 *
 * @param {{official: Dollar, mep: Dollar}} data the dollar data
 */
function updateDollar(data) {
  updateDesktop(data);
  updateMobile(data);
}

// TODO:
function updateDesktop(data) {}

// TODO:
function updateMobile(data) {}
