from contextlib import contextmanager
from typing import Optional
from decimal import Decimal
import threading

# Placeholder for valid currencies and error class
VALID_CURRENCIES = {'USD', 'EUR', 'GBP', 'JPY'}
class InvalidCurrencyError(Exception):
    pass

class CurrencyContext:
    """Thread-safe currency context manager"""
    def __init__(self):
        self._local = threading.local()
        self._global_default = 'USD'

    def get_default_currency(self) -> str:
        """Get current default currency"""
        return getattr(self._local, 'currency', self._global_default)

    def set_default_currency(self, currency: str):
        """Set default currency for current thread"""
        if currency not in VALID_CURRENCIES:
            raise InvalidCurrencyError(f"Invalid currency: {currency}")
        self._local.currency = currency

    def set_global_default(self, currency: str):
        """Set global default currency"""
        if currency not in VALID_CURRENCIES:
            raise InvalidCurrencyError(f"Invalid currency: {currency}")
        self._global_default = currency

    @contextmanager
    def currency_context(self, currency: str):
        """Temporary currency context"""
        old_currency = self.get_default_currency()
        self.set_default_currency(currency)
        try:
            yield currency
        finally:
            if hasattr(self._local, 'currency'):
                self._local.currency = old_currency
            else:
                delattr(self._local, 'currency')

# Global currency context instance
currency_context = CurrencyContext()

class AdvancedMoney:
    def __init__(self, amount, currency):
        self.amount = Decimal(amount)
        self.currency = currency

    def __add__(self, other):
        self._check_currency_match(other)
        return AdvancedMoney(self.amount + other.amount, self.currency)

    def __sub__(self, other):
        self._check_currency_match(other)
        return AdvancedMoney(self.amount - other.amount, self.currency)

    def __mul__(self, multiplier):
        return AdvancedMoney(self.amount * Decimal(multiplier), self.currency)

    def __truediv__(self, divisor):
        return AdvancedMoney(self.amount / Decimal(divisor), self.currency)

    def _check_currency_match(self, other):
        if self.currency != other.currency:
            raise ValueError("Currency mismatch")

    def __str__(self):
        return f"{self.amount:.2f} {self.currency}"

class ContextAwareMoney(AdvancedMoney):
    """Money class that uses currency context"""
    def __init__(self, amount, currency=None):
        if currency is None:
            currency = currency_context.get_default_currency()
        super().__init__(amount, currency)

    @classmethod
    def from_string(cls, amount_str: str, currency=None):
        """Create Money from string with optional currency override"""
        return cls(amount_str, currency)

# Demonstrate currency context
print("=== Currency Context Management ===")
money1 = ContextAwareMoney('100.00')
print(f"Default currency money: {money1}")
print(f"Current default currency: {currency_context.get_default_currency()}")

currency_context.set_global_default('EUR')
money2 = ContextAwareMoney('100.00')
print(f"After setting global default to EUR: {money2}")

print("\nUsing context managers:")
with currency_context.currency_context('GBP'):
    money_gbp = ContextAwareMoney('100.00')
    print(f"Inside GBP context: {money_gbp}")
    with currency_context.currency_context('JPY'):
        money_jpy = ContextAwareMoney('10000')
        print(f"Inside nested JPY context: {money_jpy}")
    money_gbp2 = ContextAwareMoney('50.00')
    print(f"Back in GBP context: {money_gbp2}")

money3 = ContextAwareMoney('75.00')
print(f"Outside context (global default): {money3}")

class ShoppingCart:
    """Shopping cart with currency context"""
    def __init__(self, store_currency='USD'):
        self.store_currency = store_currency
        self.items = []
        self.tax_rate = Decimal('0.08')

    def add_item(self, description: str, price, quantity: int = 1):
        """Add item to cart"""
        with currency_context.currency_context(self.store_currency):
            if isinstance(price, str):
                money_price = ContextAwareMoney(price)
            else:
                money_price = price
            total_price = money_price * quantity
            self.items.append({
                'description': description,
                'unit_price': money_price,
                'quantity': quantity,
                'total': total_price
            })

    def calculate_total(self):
        """Calculate cart total with tax"""
        subtotal = ContextAwareMoney('0', self.store_currency)
        for item in self.items:
            subtotal += item['total']
        tax = subtotal * self.tax_rate
        total = subtotal + tax
        return {
            'subtotal': subtotal,
            'tax': tax,
            'total': total
        }

    def display_cart(self):
        """Display cart contents"""
        print(f"\nShopping Cart ({self.store_currency}):")
        print("=" * 50)
        for item in self.items:
            if item['quantity'] == 1:
                print(f"{item['description']:<30} {item['total']}")
            else:
                print(f"{item['description']:<20} {item['quantity']} × {item['unit_price']} = {item['total']}")
        totals = self.calculate_total()
        print("-" * 50)
        print(f"{'Subtotal':<30} {totals['subtotal']}")
        print(f"{'Tax (8%)':<30} {totals['tax']}")
        print("=" * 50)
        print(f"{'TOTAL':<30} {totals['total']}")

# Demonstrate shopping cart with different currencies
print("\n=== Multi-Currency Shopping Carts ===")
us_cart = ShoppingCart('USD')
us_cart.add_item("Laptop", "999.99")
us_cart.add_item("Mouse", "29.99", 2)
us_cart.add_item("Keyboard", "79.99")
us_cart.display_cart()

eu_cart = ShoppingCart('EUR')
eu_cart.add_item("Laptop", "849.99")
eu_cart.add_item("Mouse", "24.99", 2)
eu_cart.add_item("Keyboard", "69.99")
eu_cart.display_cart()

uk_cart = ShoppingCart('GBP')
uk_cart.add_item("Laptop", "749.99")
uk_cart.add_item("Mouse", "19.99", 2)
uk_cart.add_item("Keyboard", "59.99")
uk_cart.display_cart()

class UserCurrencyPreferences:
    """Manage user currency preferences"""
    def __init__(self):
        self.user_preferences = {}

    def set_user_currency(self, user_id: str, preferred_currency: str):
        """Set user's preferred currency"""
        if preferred_currency not in VALID_CURRENCIES:
            raise InvalidCurrencyError(f"Invalid currency: {preferred_currency}")
        self.user_preferences[user_id] = preferred_currency

    def get_user_currency(self, user_id: str) -> str:
        """Get user's preferred currency"""
        return self.user_preferences.get(user_id, currency_context.get_default_currency())

    @contextmanager
    def user_context(self, user_id: str):
        """Create context for specific user"""
        user_currency = self.get_user_currency(user_id)
        with currency_context.currency_context(user_currency):
            yield user_currency

# Demonstrate user preferences
print("\n=== User Currency Preferences ===")
prefs = UserCurrencyPreferences()
prefs.set_user_currency("alice", "EUR")
prefs.set_user_currency("bob", "GBP")
prefs.set_user_currency("charlie", "JPY")
users = ["alice", "bob", "charlie", "dave"]  # dave has no preference

for user in users:
    with prefs.user_context(user):
        balance = ContextAwareMoney('1000')
        print(f"{user.capitalize()}'s balance: {balance}")