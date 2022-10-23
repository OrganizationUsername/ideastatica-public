﻿using IdeaStatiCa.BimApi.Results;
using System.Collections.Concurrent;

namespace IdeaStatica.BimApiLink.Results.BimApi
{
	public class IdeaSection : IIdeaSection
	{
		public double Position { get; }

		public IEnumerable<IIdeaSectionResult> Results => _results;

		private readonly ConcurrentBag<IIdeaSectionResult> _results = new();

		public IdeaSection(double position)
		{
			Position = position;
		}

		public void Add(IIdeaSectionResult sectionResult)
		{
			_results.Add(sectionResult);
		}
	}
}