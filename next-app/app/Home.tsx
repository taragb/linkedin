import Link from "next/link";
import { getTodos } from "./page";


export default async function Home() {
    const todos = await getTodos();
    // await prisma.todo.create({ data: { title: "test", complete: false } })
    return <>
        <header className="flex justify-between items-center mb-4">
            <h1 className="text-2xl">ToDos</h1>
            <Link className="border border-slate-300 text-slate-300 px-2 py-1 rounded hover:bg-slate-700 focus-within:bg-slate-700 outline-none" href="/new">New</Link>
        </header>
        <ul>
            {todos.map(todo => (
                <TodoItem key={todo.id} {...todo}></TodoItem>
            ))}
        </ul>
    </>;
}
