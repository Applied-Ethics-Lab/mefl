# datastructures/trees.py

class TreeNode:
    def __init__(self, value, children=None):
        self.value = value  # Could be an ethics principle, decision, etc.
        self.children = children if children else []

    def add_child(self, node):
        self.children.append(node)

    def remove_child(self, node):
        self.children = [child for child in self.children if child != node]

    def traverse_preorder(self, visit_func):
        visit_func(self)
        for child in self.children:
            child.traverse_preorder(visit_func)

    def traverse_postorder(self, visit_func):
        for child in self.children:
            child.traverse_postorder(visit_func)
        visit_func(self)

    def find(self, predicate):
        if predicate(self):
            return self
        for child in self.children:
            found = child.find(predicate)
            if found:
                return found
        return None

# Ethics Decision Tree Node
class EthicsDecisionNode(TreeNode):
    def __init__(self, question, options, decision=None):
        """
        question: str - question asked at this node
        options: dict[str, EthicsDecisionNode] - map from option string to next node
        decision: optional final decision or ethical conclusion at leaf
        """
        super().__init__(question)
        self.options = options  # key: option string, value: next node
        self.decision = decision

    def evaluate(self, context):
        """
        context: dict of variables representing current situation
        returns: ethical decision or None if not decided yet
        """
        if self.decision is not None:
            return self.decision

        # Example: determine option based on context
        # This part should be customized based on how you want to evaluate options
        for option, node in self.options.items():
            # Your logic to select the right option based on context
            if self._option_matches_context(option, context):
                return node.evaluate(context)
        return None

    def _option_matches_context(self, option, context):
        # Placeholder for matching logic
        # You can extend this for complex decision logic
        return option in context.get('choices', [])

# Example usage:
if __name__ == "__main__":
    leaf1 = EthicsDecisionNode(None, {}, decision="Ethically acceptable")
    leaf2 = EthicsDecisionNode(None, {}, decision="Ethically questionable")
    root = EthicsDecisionNode(
        "Is action legal?",
        {
            "yes": leaf1,
            "no": leaf2
        }
    )

    context = {'choices': ['yes']}
    print("Decision:", root.evaluate(context))
