import csv
def read_transactions(csv_file):
    transactions = []
    with open(csv_file, mode='r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader) 
        for row in csv_reader:
            valid_items = []
            for item in row[1:]:
                cleaned_item = item.strip()
                if cleaned_item:
                    valid_items.append(cleaned_item)
            transactions.append(valid_items)
    return transactions

def generate_combinations(items, n):
    if n == 0:
        return [[]]
    if len(items) < n:
        return []
    if len(items) == n:
        return [items]
    result = []
    for i in range(len(items)):
        first = items[i:i+1]
        remaining = generate_combinations(items[i+1:], n-1)
        for comb in remaining:
            result.append(first + comb)
    return result

def calculate_support(itemset, transactions):
    count = 0
    for transaction in transactions:
        all_items_present = True
        for item in itemset:
            if item not in transaction:
                all_items_present = False
                break
        if all_items_present:
            count += 1
    return (count / len(transactions)) * 100

def find_frequent_itemsets(transactions, min_support):
    unique_items = list(set(item for transaction in transactions for item in transaction))
    frequent_itemsets = []
    for i in range(1, len(unique_items) + 1):
        combinations = generate_combinations(unique_items, i)
        for itemset in combinations:
            support = calculate_support(itemset, transactions)
            if support >= min_support:
                frequent_itemsets.append((itemset, support))
    return frequent_itemsets

def run_frequent_itemset_mining(csv_file, min_support):
    transactions = read_transactions(csv_file)
    frequent_itemsets = find_frequent_itemsets(transactions, min_support)
    print("\nFrequent Itemsets with Support (as Percentage):")
    if frequent_itemsets:
        for itemset, support in frequent_itemsets:
            print(f"{itemset}: {support:.2f}%")
    else:
        print("No frequent itemsets found with the given minimum support.")

csv_file = (r"C:\Users\bhilw\OneDrive\Documents\DM\7_association_rule\data.csv")
min_support = float(input("Enter the minimum support (in percentage): "))
run_frequent_itemset_mining(csv_file, min_support)
