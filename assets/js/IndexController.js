/**
 * IndexController.js
 *
 * @file  The Index Controller
 * @author Tomás Sánchez
 * @since  06.12.2022
 */

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
  fetch("https://www.dolarsi.com/api/api.php?type=valoresprincipales")
    .then((data) =>
      data
        .json()
        .then((result) => {
          let oData = { official: new Dollar(), mep: new Dollar() };
          // Info:
          result = result.map((x) => x.casa);

          let official = result.find((x) => x.nombre == "Dolar Oficial");
          let mep = result.find((x) => x.nombre == "Dolar Bolsa");

          oData.official = new Dollar(official?.compra, official?.venta);
          oData.mep = new Dollar(mep?.compra, mep?.venta);

          updateDollar(result);
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
  // updateDesktop(data);
  // updateMobile(data);
}

// TODO:
function updateDesktop(data) {}
// TODO:
function updateMobile(data) {}
