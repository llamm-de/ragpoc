from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped, Session
from sqlalchemy import String, create_engine

class Base(DeclarativeBase):
    pass

class Post(Base):
    __tablename__ = "posts"

    id:Mapped[int] = mapped_column(primary_key=True)
    title:Mapped[str] = mapped_column(String(30))
    content:Mapped[str] = mapped_column(String())

    def __repr__(self) -> str:
        return f"Blog post(id={self.id}, title={self.title})"

def main():

    DB_PATH="sqlite:///trials/data/test.db"

    # Create database connection
    engine = create_engine(DB_PATH, echo=True)
    Base.metadata.create_all(engine)
    with Session(engine) as session:
        trial_post = Post(
            title = "test",
            content = "Lorem ipsum"
        )
        
        session.add(trial_post)
        session.commit()

if __name__ == "__main__":
    main()