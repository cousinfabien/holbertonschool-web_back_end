export default class Currency {
  constructor(code, name) {
    this._code = code;
    this._name = name;
  }

  // Getter et Setter pour 'code'
  get code() {
    return this._code;
  }

  set code(value) {
    if (typeof value !== 'string') throw new TypeError('Code must be a string');
    this._code = value;
  }

  // Getter et Setter pour 'name'
  get name() {
    return this._name;
  }

  set name(value) {
    if (typeof value !== 'string') throw new TypeError('Name must be a string');
    this._name = value;
  }

  // Méthode d'instance
  displayFullCurrency() {
    return `${this._name} (${this._code})`;
  }
}
