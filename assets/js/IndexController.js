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
// FUNCTION APIS

window.onload = BuyBlue()
function BuyBlue() {
 var buy = document.getElementById("dolar-blue-hoy-compra")
 fetch(API_URL)
    .then(Response => Response.json())
    .then(data => {
      console.log(data.result)
      buy.innerHTML += `
      <b>$<span id="dolar-blue-hoy-compra">${data[1].casa.venta}</span></b>
      `
    })
  }
function BuyBlue() {
  var buy = document.getElementById("dolar-blue-hoy-compra")
  fetch(API_URL)
   .then(Response => Response.json())
   .then(data => {
     console.log(data.result)
     buy.innerHTML += `
     <b>$<span id="dolar-blue-hoy-compra">${data[1].casa.compra}</span></b>
       `
    })
}
// TODO:
function updateDesktop(data) {}

// TODO:
function updateMobile(data) {}
