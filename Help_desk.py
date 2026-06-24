class SupportTicketNode:
    def __init__(self, priority: int, description: str):
        self.priority: int = priority
        self.description: str = description
        self.left: 'SupportTicketNode' | None = None
        self.right: 'SupportTicketNode' | None = None

class PriorityQueueTree:
    def __init__(self):
        self.root: SupportTicketNode | None = None

    def add_ticket(self, priority: int, description: str) -> None:
 
        if self.root is None:
            self.root = SupportTicketNode(priority, description)
        else:
            self._add_recursive(self.root, priority, description)

    def _add_recursive(self, current_node: SupportTicketNode, priority: int, description: str) -> None:
       
        if priority > current_node.priority:
            if current_node.right is None:
                current_node.right = SupportTicketNode(priority, description)
            else:
                self._add_recursive(current_node.right, priority, description)
    
        else:
            if current_node.left is None:
                current_node.left = SupportTicketNode(priority, description)
            else:
                self._add_recursive(current_node.left, priority, description)

    def resolve_highest_priority(self) -> None:
    
        if self.root is None:
            print("Nenhum chamado pendente na fila no momento.")
            return

        highest_ticket = self._find_max_priority_node(self.root)
        print(f"Resolvendo Chamado: [Prioridade {highest_ticket.priority}] - {highest_ticket.description}")

        self.root = self._remove_node(self.root, highest_ticket.priority)

    def _find_max_priority_node(self, current_node: SupportTicketNode) -> SupportTicketNode:
       
        while current_node.right is not None:
            current_node = current_node.right
        return current_node

    def _remove_node(self, current_node: SupportTicketNode | None, priority: int) -> SupportTicketNode | None:
        
        if current_node is None:
            return None

        if priority < current_node.priority:
            current_node.left = self._remove_node(current_node.left, priority)
        elif priority > current_node.priority:
            current_node.right = self._remove_node(current_node.right, priority)
        else:
           
            if current_node.left is None:
                return current_node.right
            elif current_node.right is None:
                return current_node.left

            successor_node = self._find_min_priority_node(current_node.right)
            current_node.priority = successor_node.priority
            current_node.description = successor_node.description
            
            current_node.right = self._remove_node(current_node.right, successor_node.priority)

        return current_node

    def _find_min_priority_node(self, current_node: SupportTicketNode) -> SupportTicketNode:
       
        while current_node.left is not None:
            current_node = current_node.left
        return current_node

    def print_pending_tickets(self) -> None:

        print("\n--- Chamados Pendentes (Ordem de Urgência) ---")
        if self.root is None:
            print("Fila vazia.")
        else:
            self._print_in_order_reverse(self.root)
        print("----------------------------------------------\n")

    def _print_in_order_reverse(self, current_node: SupportTicketNode | None) -> None:

        if current_node is not None:
            self._print_in_order_reverse(current_node.right)
            print(f"Prioridade: {current_node.priority:02d} | Descrição: {current_node.description}")
            self._print_in_order_reverse(current_node.left)

help_desk_queue = PriorityQueueTree()

help_desk_queue.add_ticket(10, "Mouse não está funcionando.")
help_desk_queue.add_ticket(35, "Não lembro minha senha.")
help_desk_queue.add_ticket(100, "Servidor caiu.")
help_desk_queue.add_ticket(45, "Instalar pacote Office na máquina 0845.")
help_desk_queue.add_ticket(75, "Falha de segurança detectada no firewall.")

help_desk_queue.print_pending_tickets()

help_desk_queue.resolve_highest_priority()
help_desk_queue.resolve_highest_priority()

help_desk_queue.print_pending_tickets()