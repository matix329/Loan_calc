# Kalkulator Kredytowy

Kalkulator Kredytowy to narzędzie wiersza poleceń napisane w Pythonie, które umożliwia obliczanie różnych aspektów kredytu, takich jak wysokość miesięcznej raty, kwota główna kredytu, liczba okresów potrzebnych do spłaty kredytu lub kwota nadpłaty.

## Użycie

To narzędzie obsługuje dwa rodzaje obliczeń płatności:

1. **Płatności w ratach stalych**
2. **Płatności w ratach malejacych**

### Argumenty wiersza poleceń

Program akceptuje następujące argumenty wiersza poleceń:

- `--type`: Rodzaj obliczeń płatności. Może to być `annuity` (raty stałe) lub `diff` (raty różnicowane). Ten argument jest wymagany.
- `--principal`: Kwota główna kredytu (kwota, którą chcesz pożyczyć).
- `--payment`: Kwota miesięcznej raty.
- `--periods`: Liczba okresów (miesięcy), w ciągu których kredyt będzie spłacany.
- `--interest`: Roczna stopa procentowa (np. `10` dla 10%). Ten argument jest wymagany i musi być dodatni.

### Zasady ogólne

- W przypadku **Płatności stale** (`--type=annuity`) musisz podać dokładnie trzy z czterech parametrów: `--principal`, `--payment`, `--periods`, `--interest`. Program obliczy brakujący czwarty parametr.
- W przypadku **Płatności malejace** (`--type=diff`) musisz podać `--principal`, `--periods` oraz `--interest`. Parametr `--payment` nie jest używany w tym przypadku.

### Przykłady użycia

1. **Obliczanie kwoty głównej kredytu**:

   ```sh
   python creditcalc.py --type=annuity --payment=8722 --periods=120 --interest=5.6
   ```

   **Wynik**:

   ```
   Your loan principal = 800018!
   Overpayment = 246622
   ```

2. **Obliczanie wysokości miesięcznej raty**:

   ```sh
   python creditcalc.py --type=annuity --principal=1000000 --periods=60 --interest=10
   ```

   **Wynik**:

   ```
   Your annuity payment = 21248!
   Overpayment = 274880
   ```

3. **Obliczanie liczby okresów**:

   ```sh
   python creditcalc.py --type=annuity --principal=500000 --payment=23000 --interest=7.8
   ```

   **Wynik**:

   ```
   It will take 2 years and 1 month to repay this loan!
   Overpayment = 60360
   ```

4. **Obliczanie rat różnicowanych**:

   ```sh
   python creditcalc.py --type=diff --principal=1000000 --periods=10 --interest=10
   ```

   **Wynik**:

   ```
   Month 1: payment is 108334
   Month 2: payment is 107500
   Month 3: payment is 106667
   Month 4: payment is 105834
   Month 5: payment is 105000
   Month 6: payment is 104167
   Month 7: payment is 103334
   Month 8: payment is 102500
   Month 9: payment is 101667
   Month 10: payment is 100834

   Overpayment = 45837
   ```

### Zasady walidacji

- Jeśli zostaną podane niepoprawne argumenty lub brakuje wymaganych parametrów, program wyświetli komunikat "Incorrect parameters". Na przykład:

  ```sh
  python creditcalc.py --type=annuity --principal=1000000 --payment=104000
  ```

  **Wynik**:

  ```
  Incorrect parameters
  ```

---
