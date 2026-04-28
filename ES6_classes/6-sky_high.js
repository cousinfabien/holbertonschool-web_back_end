import Building from './5-building';

export default class SkyHighBuilding extends Building {
  constructor(sqft, floors) {
    // Appelle le constructeur de la classe parente (Building)
    super(sqft);
    this._floors = floors;
  }

  // Getter pour 'sqft' hérité de Building, mais on peut ajouter celui de floors
  get floors() {
    return this._floors;
  }

  // Surcharge de la méthode imposée par la classe parente
  evacuationWarningMessage() {
    return `Evacuate slowly the ${this._floors} floors`;
  }
}
