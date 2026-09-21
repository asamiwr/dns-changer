import sys

from app.application import DNSChanger

if __name__ == "__main__":
    app = DNSChanger()
    app.run(sys.argv)
