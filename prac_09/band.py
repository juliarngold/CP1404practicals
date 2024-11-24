class Band:
    """Represent a Band object."""

    def __init__(self, name):
        """Initialise a Band instance."""
        self.name = name
        self.members = []

    def __str__(self):
        members_info = ", ".join([str(member) for member in self.members])
        return f"{self.name} ({members_info})"

    def add(self, member):
        """Add a band member."""
        self.members.append(member)

    def play(self):
        """Return the member and its instrument and cost"""
        return "\n".join([member.play() for member in self.members])