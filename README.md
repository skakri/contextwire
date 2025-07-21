# ContextWire

## UWAGA: this README.md is a placeholder and meant (for now) as a rough draft

### A Gloriously Over-Engineered Hardware Automation Framework

> Probably a huge mistake.
> But like, a powerful, scripted, glorious mistake.

ContextWire is your new hardware automation overlord. 
It aims to talk to **Saleae**, **Bus Pirate**, 
**Simplicity Commander**, and even your dusty **LXI o-scope**, 
all from one place. No more juggling 17 terminals and making 
ritual sacrifices to the demo gods — just a single, 
unified interface to script, control, and automate your lab gear.

## ⚠️ Current Status: Alpha AF

This project is in the very early stages of development. 
Expect bugs, breaking changes, and moments of existential dread. 
If it works, it's a miracle. If it breaks, you get to keep both pieces.

## ✨ Core Features

* **💬 Unified Control:** Access all your tools through a REST API, 
WebSockets, or the Model Context Protocol (MCP) 
for agentic AI interactions.
* **🔌 Modular Drivers:** A plug-and-play architecture makes it 
easy to add new hardware. If it has a port, we can probably talk to it. 
Eventually.
* **🧪 Built for Embedded Devs:** Perfect for anyone who is sick 
of vendor-specific GUIs and wants to script their hardware interactions.
* **🔧 Built with Python:** Because I hate myself just enough.

## 🚀 Getting Started

*(This section is a placeholder for when things actually work.)*

**1. Installation (Theoretically):**

```
git clone https://github.com/skakri/contextwire.git
cd contextwire
# ???
cd ..
rm -rf contextwire
```

**2. Configuration:**

Copy the example environment file and pretend to fill it out.

```
cp .env.example .env
```

**3. Run It:**

Launch the server and pray (we use Python 3.x as default here, 
don't be a caveman).

```
python -m contextwire.main --run-api --run-ws
```

## 🚦 Run Modes

ContextWire can be launched in several modes, simultaneously if you're 
feeling brave:

* **Stateful MCP Server:** A server implementing the 
Model Context Protocol, allowing agentic AI systems to maintain and 
interact with hardware state and context.
* **REST API Server:** For stateless, command-based control. 
Perfect for integration with scripts and CI/CD pipelines.
* **WebSocket Server:** For real-time, bidirectional communication. 
Stream live data or build interactive remote shells.

## 📦 Planned Device Support

| **Device / Interface** | **Status** | **Notes** |
| --- | --- | --- |
| Saleae Logic Analyzer | 🔜 `WIP` | `logic2-automation` library |
| Simplicity Commander | ➡️ `Up Next` | Wrapping the `commander` CLI |
| Bus Pirate | ❓ `Planned` | Binary bitbang mode |
| LXI Instruments | 🤯 `Maybe` | via `lxi-tools` or similar |
| Sigrok-Supported Devices | 🤯 `Maybe` | The holy grail of driver support |

## 🤝 How to Contribute

Found a bug? Have a brilliant idea? 
Want to add support for a new device? Excellent.

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-awesome-idea`).
3. Make your changes.
4. Submit a pull request and tell me what you broke.

## 📜 License

Licensed under the **Apache 2.0 License**.

> Made with poor life choices.
> Also yes, I wrote parts of this README by wasting tokens 
because I couldn't be bothered to write it myself.
> ~~No regrets~~ Some regrets.
