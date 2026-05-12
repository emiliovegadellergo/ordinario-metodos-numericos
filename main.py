"""Aplicación CLI para métodos numéricos del parcial 2."""


class MainApplication:
    """Punto de entrada principal de la aplicación de métodos numéricos."""

    MENU = {
        "1": "Serie de Maclaurin",
        "2": "Newton-Raphson",
        "3": "Interpolación",
        "4": "Salir",
    }

    def run(self) -> None:
        """Inicia el bucle principal de la aplicación."""
        print("=== Métodos Numéricos — Parcial 2 ===\n")
        while True:
            self._print_menu()
            opcion = input("Selecciona una opción: ").strip()
            print()

            if opcion == "1":
                self._serie_maclaurin()
            elif opcion == "2":
                self._newton_raphson()
            elif opcion == "3":
                self._interpolacion()
            elif opcion == "4":
                print("Saliendo...")
                break
            else:
                print("Opción no válida. Intenta de nuevo.\n")

    # ------------------------------------------------------------------
    # Métodos privados
    # ------------------------------------------------------------------

    def _print_menu(self) -> None:
        """Imprime las opciones del menú en pantalla."""
        print("--- Menú ---")
        for clave, nombre in self.MENU.items():
            print(f"  {clave}. {nombre}")
        print()

    def _serie_maclaurin(self) -> None:
        """Módulo de Serie de Maclaurin (pendiente de implementación)."""
        print("En construcción\n")

    def _newton_raphson(self) -> None:
        """Módulo de Newton-Raphson (pendiente de implementación)."""
        print("En construcción\n")

    def _interpolacion(self) -> None:
        """Módulo de Interpolación (pendiente de implementación)."""
        print("En construcción\n")


if __name__ == "__main__":
    app = MainApplication()
    app.run()
