export default class Airport {
  constructor(name, code) {
    this._name = name;
    this._code = code;
  }

  // Getter pour le nom (optionnel selon l'énoncé, mais bonne pratique)
  get name() {
    return this._name;
  }

  // Getter pour le code
  get code() {
    return this._code;
  }

  // Cette méthode définit l'étiquette de l'objet pour toString()
  get [Symbol.toStringTag]() {
    return this._code;
  }
}
