## History
### Just Libraries
OS would provide API. Jobs set up and then run in a `batch` by the operator. Computers were not interactive.

### Protection
The idea of `system call` invented by Atlas computing system. Instead of providing OS routines as a library (`procedure call`), special instructions to transition into a more formal, controlled process.

{{<mermaid>}}
sequenceDiagram
    participant U as User Mode
    participant K as Kernel Mode
    U->>K: trap
    K->>U: return-from-trap
{{</mermaid>}}

### Multiprogramming
I/O devices were slow, having a program wait CPU was a waste of time. Memory protection and concurrency became critical in the presence of I/O and interrupts. Unix was introduced inspired by TENEX and Berkeley Time-Sharing System.

### Modern Era
DOS didn’t think memory protection was important; thus, a malicious application could scribble all over memory. Mac OS(v9 and earlier) took a cooperative approach to job scheduling; thus, a thread that accidentally got stuck in an infinite loop could take over the entire system, forcing a reboot.

## The Process
**Time sharing** allows OS to share CPU resource, by **context-switch** (stop a program to run another). A **scheduling policy** let OS to decide which program to run.

**Address space** is the memory the process can address, registers are also part of process's machine state. For example **program counter (PC, or instruction pointer IP)** tells which instruction to execute next, **stack pointer** and associated **frame pointer** are used to manage the stack for function parameters, local variables and return addresses.
![](attachments/2021-04-28-12-29-07_program_to_process.png)

In early OSes loading done eagerly, modern OSes perform it lazily by **paging** and **swapping**.
### Process States
{{<mermaid>}}
stateDiagram-v2
    Running --> Ready : Descheduled
    Ready --> Running : Scheduled
    Running --> Blocked : I/O initiate
    Blocked --> Ready : I/O done
{{</mermaid>}}
**Running**: executing instructions  
**Ready**: ready, but OS has chosen not to run  
**Blocked**: not ready. I/O request etc.  
These decisions are made by OS **scheduler**.

| Time | Process<sub>0</sub> | Process<sub>1</sub> | Notes                     |
| ---- | ----------- | ----------- | ------------------------- |
| 1    | Running     | Ready       |
| 2    | Running     | Ready       |
| 3    | Running     | Ready       | Process<sub>0</sub> /subinit>ates I/O |
| 4    | Blocked     | Running     | Process<sub>0</sub> is blocked,   |
| 5    | Blocked     | Running     | so Process<sub>1</sub> runs       |
| 6    | Blocked     | Running     |
| 7    | Ready       | Running     | I/O done                  |
| 8    | Ready       | Running     | Process<sub>1</sub> now done      |
| 9    | Running     | –           |
| 10   | Running     | –           | Process<sub>0</sub> now done      |

### Process API
**Shell** run code after the call to `fork()` (to create a new child process by copying parent) but before the call to `exec()` (to run the command); this code can alter the environment of the about-to-be-run program, and then waits for the command to complete by calling `wait()`. When the child completes, shell returns, ready for next command. This enables features like input/output redirection, pipes.

Each process has a name, in most systems a number, **process ID (PID)**. Control is available in the form of **signals** to stop, continue, terminate.

The control is encapsulated by the notion of **user**, whom can only control their own processes. A **superuser** can control all processes.