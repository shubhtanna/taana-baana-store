// Size picker: fills the size options from the product's sizes and shows them as buttons.
(function () {
  var select = document.getElementById('size');
  var box = document.getElementById('size-buttons');
  if (!select || !box) return;
  var sizes = JSON.parse(select.dataset.sizes || '[]');
  var soldout = JSON.parse(select.dataset.soldout || '[]');

  sizes.forEach(function (s) {
    var out = soldout.indexOf(s) !== -1;
    var opt = document.createElement('option');
    opt.value = s;
    opt.textContent = s + (out ? ' (sold out)' : '');
    opt.disabled = out;
    select.appendChild(opt);

    var b = document.createElement('button');
    b.type = 'button';
    b.textContent = s;
    b.disabled = out;
    b.onclick = function () {
      select.value = s;
      box.querySelectorAll('button').forEach(function (x) { x.classList.toggle('on', x === b); });
    };
    box.appendChild(b);
  });

  // One-size items need no choice.
  var available = sizes.filter(function (s) { return soldout.indexOf(s) === -1; });
  if (available.length === 1) box.querySelector('button:not([disabled])').click();
  select.closest('label').classList.add('enhanced');
})();
