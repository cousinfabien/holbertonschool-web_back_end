import Currency from './3-currency';

export default class Pricing {
  constructor(amount, currency) {
    this._amount = amount;
    this._currency = currency;
  }

  // Getter et Setter pour 'amount'
  get amount() {
    return this._amount;
  }

  set amount(value) {
    if (typeof value !== 'number') throw new TypeError('Amount must be a number');
    this._amount = value;
  }

  // Getter et Setter pour 'currency'
  get currency() {
    return this._currency;
  }

  set currency(value) {
    if (!(value instanceof Currency)) throw new TypeError('Currency must be an instance of Currency');
    this._currency = value;
  }

  // Méthode d'instance
  displayFullPrice() {
    return `${this._amount} ${this._currency.name} (${this._currency.code})`;
  }

  // Méthode statique
  static convertPrice(amount, conversionRate) {
    if (typeof amount !== 'number') throw new TypeError('Amount must be a number');
    if (typeof conversionRate !== 'number') throw new TypeError('Conversion rate must be a number');
    return amount * conversionRate;
  }
}
