class SLRParser:
    def __init__(self, grammar, terminals, non_terminals, start_symbol, parsing_table):
        self.grammar = grammar
        self.terminals = terminals
        self.non_terminals = non_terminals
        self.start_symbol = start_symbol
        self.parsing_table = parsing_table

    def parse(self, input_string):
        stack = [0]  # Initial state
        input_string += "$"  # Append end marker
        pointer = 0  # Start of input

        print(f"{'Stack':<20}{'Input':<20}{'Action':<20}")
        print("-" * 60)

        while True:
            state = stack[-1]  # Get the top of the stack
            current_symbol = input_string[pointer]

            if current_symbol not in self.parsing_table[state]:
                raise ValueError(f"Error: Unexpected symbol '{current_symbol}' at position {pointer}")

            action = self.parsing_table[state][current_symbol]

            # Format stack and input for readability
            stack_str = " ".join(map(str, stack))
            input_str = input_string[pointer:]

            print(f"{stack_str:<20}{input_str:<20}{action:<20}")

            if action == "ACCEPT":
                print("\nParsing successful!")
                return True

            elif action.startswith("S"):  # Shift
                # Extract the next state to shift to
                next_state = int(action[1:])
                stack.append(next_state)  # Push new state onto the stack
                pointer += 1  # Move input pointer forward

            elif action.startswith("R"):  # Reduce
                # Extract the production index for the reduce action
                production_index = int(action[1:])
                if production_index >= len(self.grammar) or production_index < 0:
                    raise ValueError(f"Invalid production index: {production_index}")

                lhs, rhs = self.grammar[production_index]

                # Pop |rhs| symbols from the stack
                for _ in range(len(rhs)):
                    stack.pop()

                # Get the state at the new top of the stack
                top_state = stack[-1]

                if lhs not in self.parsing_table[top_state]:
                    raise ValueError(f"Invalid LHS '{lhs}' after reduction at state {top_state}")

                # Push the new state for the LHS of the production
                stack.append(self.parsing_table[top_state][lhs])

            else:
                raise ValueError(f"Invalid action: {action}")


# Define the grammar, parsing table, and input string
grammar = [
    ("S", ["A", "A"]),  # Production 0: S -> AA
    ("A", ["a"]),       # Production 1: A -> a
]

terminals = ["a"]
non_terminals = ["S", "A"]
start_symbol = "S"

parsing_table = {
    0: {"a": "S2", "S": 1, "A": 3},
    1: {"$": "ACCEPT"},
    2: {"a": "S2", "$": "R2", "A": 4},  # Add handling for '$' in state 2
    3: {"a": "R1", "$": "R1"},
    4: {"a": "R2", "$": "R2"},
}

input_string = "aa"

# Instantiate the parser and parse the string
parser = SLRParser(grammar, terminals, non_terminals, start_symbol, parsing_table)
parser.parse(input_string)
