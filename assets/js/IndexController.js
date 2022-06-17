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

window.onload = officialDolarBuy()
function officialDolarBuy() {
  var officialBuy = document.getElementById("dolar-oficial-hoy-compra")
  fetch(API_URL)
     .then(Response => Response.json())
     .then(data => {
       console.log(data.result)
       officialBuy.innerHTML += `
       <b><span id="dolar-oficial-hoy-compra">${data[0].casa.compra}</span></b>
       `
     })
   }
window.onload = officialDolarSell()
function officialDolarSell() {
  var officialVenta = document.getElementById("dolar-oficial-hoy-venta")
  fetch(API_URL)
     .then(Response => Response.json())
     .then(data => {
       console.log(data.result)
       officialVenta.innerHTML += `
       <b><span id="dolar-oficial-hoy-venta">${data[0].casa.venta}</span></b>
       `
     })
   }
window.onload = SellBlue()
function SellBlue() {
  var blueVenta = document.getElementById("dolar-blue-hoy-venta")
  fetch(API_URL)
     .then(Response => Response.json())
     .then(data => {
       console.log(data.result)
       blueVenta.innerHTML += `
       <b>$<span id="dolar-blue-hoy-venta">${data[1].casa.venta}</span></b>
       `
     })
   }
window.onload = BuyBlue()
function BuyBlue() {
 var blueCompra = document.getElementById("dolar-blue-hoy-compra")
 fetch(API_URL)
    .then(Response => Response.json())
    .then(data => {
      console.log(data.result)
      blueCompra.innerHTML += `
      <b>$<span id="dolar-blue-hoy-compra">${data[1].casa.compra}</span></b>
      `
    })
  }
  window.onload = ContadoConLiqui()
  function ContadoConLiqui() {
    var ContLiqui = document.getElementById("contado-referencia")
    fetch(API_URL)
       .then(Response => Response.json())
       .then(data => {
         console.log(data.result)
         ContLiqui.innerHTML += `
         <b>$<span id="contado-referencia">${data[3].casa.venta}</span></b>
         `
       })
     }

  
function updateDesktop(data) {}

// TODO:
function updateMobile(data) {}
